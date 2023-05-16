from django.shortcuts import render, redirect
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
                return redirect('pasajera')
        else:
            identUser = []
            passworkUser = []
            for i in listUser:
                identUser.append(i.identificacion_usu)
                passworkUser.append(i.contraseña)

            identificacion_user = Registro.get("identificacionLog")
            contraseña_user= Registro.get("contrasenaLog")
        
            for j in  identUser:
                if identificacion_user == str(j):
                    passwork = Usuaria.objects.get(identificacion_usu=j).contraseña
                    if passwork == contraseña_user:
                        return pasajera(request)
                    else:
                        messages.success(request, "Usuaria o contraseña incorrectas")
                        print("Usuaria o contraseña incorrectas")
                else:
                    messages.success(request, "Usuaria o contraseña incorrectas")
                    print("Usuaria o contraseña incorrectas")
        
    return render(request, 'index.html')



def signinCond(request):
    if request.method == 'POST':
        formRegistroCond= RegistroCoductorasForm(request.POST)
        if formRegistroCond.is_valid():
            nombre = request.POST.get("nombre")
            identificacion = request.POST.get("identificacion")
            celular = request.POST.get("celular")
            correo = request.POST.get("correo")
            contraseña= request.POST.get("contraseña")
            

            usuaria= Conductora(nombre_cond=nombre, identificacion_cond=identificacion, celular= celular, correo= correo, contraseña= contraseña, placa_carro="")
            usuaria.save()
            
            return redirect('pasajera')
    else:
        formRegistroCond = RegistroCoductorasForm()
    context =  {'formRegistroCond':formRegistroCond}
    return render(request, "signinCond.html ", context)



def pasajera(request):
    objetos= Usuaria.objects.all()
    Info ={'objetos': objetos}
    return render(request, "pasajera.html ", Info)