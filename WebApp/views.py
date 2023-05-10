from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from .forms import *

def index(request):
    if request.method == 'POST':
        formRegistro= RegistroUsuariaForm(request.POST)
        if formRegistro.is_valid():
            nombre = request.POST.get("nombre")
            identificacion = request.POST.get("identificacion")
            celular = request.POST.get("celular")
            correo = request.POST.get("correo")
            contraseña= request.POST.get("contraseña")

            usuaria= Usuaria(nombre_usu=nombre, identificacion_usu=identificacion, celular= celular, correo= correo, contraseña= contraseña)
            usuaria.save()
           
            return redirect('pasajera')
    else:
        formRegistro = RegistroUsuariaForm()
    context =  {'formRegistro':formRegistro}
    return render(request, 'index.html', context)



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