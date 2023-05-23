from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

def index(request):
    if request.method == 'POST':
        listUser = Usuaria.objects.all()
        Registro = request.POST
        
        if Registro.get("identificacion") != None:
            nombre = Registro.get("Nombre")
            identificacion = Registro.get("identificacion")
            celular = Registro.get("celular")
            correo = Registro.get("correo")
            contraseña= Registro.get("password")

            prymaryUser = []
            
            for k in listUser:
                prymaryUser.append(str(k.identificacion_usu))

            if identificacion in prymaryUser:
                messages.success(request, "La cuenta que acaba de registrar ya existe")
                print("cuenta ya existe")
                
            else:
                usuaria= Usuaria(nombre_usu=nombre, identificacion_usu=identificacion, celular= celular, correo= correo, contraseña= contraseña)
                usuaria.save() 
                return redirect('pasajera', identificacion=usuaria.identificacion_usu)
        else:
            identificacion_user = Registro.get('identificacionLog')
            contraseña_user = Registro.get('contrasenaLog')

            try:
                usuaria = Usuaria.objects.get(identificacion_usu=identificacion_user, contraseña=contraseña_user)
                return redirect('pasajera', identificacion=usuaria.identificacion_usu)
            except Usuaria.DoesNotExist:
                messages.error(request, "Usuaria o contraseña incorrectas")
        
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def signinCond(request):
    if request.method == 'POST':
        formRegistroCarros= RegistroCarrosForm(request.POST)
        if formRegistroCarros.is_valid():
            placa = request.POST.get("placa")
            marca = request.POST.get("marca")
            modelo = request.POST.get("modelo")
            papeles = "si"
            

            carros= Carro(placa_carro=placa, marca=marca, modelo= modelo, papeles= papeles)
            carros.save()
            return redirect('signupC')
    else:
        formRegistroCarros = RegistroCarrosForm()
    context =  {'formRegistroCarros':formRegistroCarros}
    return render(request, "signinCond.html ", context)

def signupC(request):
    if request.method == 'POST':
        formRegistroConductoras= RegistroCoductorasForm(request.POST)
        if formRegistroConductoras.is_valid():
            nombre = request.POST.get("nombre")
            identificacion = request.POST.get("identificacion")
            celular = request.POST.get("celular")
            correo=request.POST.get("correo")
            contraseña=request.POST.get("contraseña")
            placa_carro = request.POST.get("placa")
            carro = Carro.objects.get(placa_carro=placa_carro)
            

            Conductoras= Conductora(identificacion_cond=identificacion, nombre_cond=nombre, correo= correo, contraseña= contraseña, celular=celular,placa_carro=carro)
            Conductoras.save()
            identificacion_cond = Conductoras.identificacion_cond
        
            return redirect('conductoras', identificacion_cond=identificacion_cond)
            #return redirect('conductoras', args=[nombre, identificacion])
    else:
        formRegistroConductoras = RegistroCoductorasForm()
    context =  {'formRegistroConductoras':formRegistroConductoras}
    return render(request, "signupC.html", context)


def solicitar_viaje(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de solicitud de viaje
        origen = request.POST.get('origen')
        destino = request.POST.get('destino')
        precio = int(request.POST.get('price'))
        distancia = int(request.POST.get('distance'))
        tiempo = request.POST.get('duration')
        identificacion_user = request.POST['identificacion_user']
        contraseña_user = request.POST['contraseña_user']

        print(origen)
        print(destino)
        print(precio)
        print(distancia)
        print(tiempo)
        print(identificacion_user)
        print(contraseña_user)
        
        # Obtener la usuaria autenticada
        try:
            usuaria = Usuaria.objects.get(identificacion_usu=identificacion_user, contraseña=contraseña_user)
        except Usuaria.DoesNotExist:
            messages.error(request, "Usuaria o contraseña incorrectas")
            return redirect('index')

        # Obtener todas las conductoras disponibles
        conductoras_disponibles = Conductora.objects.all()

        for conductora in conductoras_disponibles:
            # Crear el objeto Viaje para cada conductora
            viaje = Viaje.objects.create(
                identificacion_usu=usuaria.identificacion_usu,
                identificacion_cond=conductora,
                origen=origen,
                destino=destino,
                precio=precio,
                distancia=distancia,
                tiempo=tiempo
            )

        messages.success(request, 'Viaje solicitado correctamente')
        return redirect('pasajera', identificacion=usuaria.identificacion_usu)



def pasajera(request, identificacion):
    usuaria = Usuaria.objects.get(identificacion_usu=identificacion)
    viajes = Viaje.objects.filter(identificacion_usu=usuaria).select_related('identificacion_cond')
    
    if request.method == 'POST':
        form = UsuariaForm(request.POST, instance=usuaria)
        if form.is_valid():
            form.save()
            return redirect('pasajera', identificacion=identificacion)
    else:
        form = UsuariaForm(instance=usuaria)
    return render(request, "pasajera.html ",{'usuaria': usuaria, 'form': form, 'viajes': viajes})

def conductoras(request, identificacion_cond):
    conductora = Conductora.objects.get(identificacion_cond=identificacion_cond)
    viajes_pendientes = Viaje.objects.filter(identificacion_cond=None).select_related('identificacion_usu')
    context = {
        'viajes_pendientes': viajes_pendientes,
        'conductora': conductora,
    }
    if request.method == 'POST' and 'aceptar_viaje' in request.POST:
        viaje_id = request.POST.get('aceptar_viaje')
        viaje = Viaje.objects.get(id=viaje_id)

        # Asignar la conductora al viaje
        viaje.identificacion_cond = Conductora.objects.get(identificacion_cond=identificacion_cond)
        viaje.save()

        return redirect('conductoras', identificacion_cond=identificacion_cond)

    return render(request, "conductoras.html", context)