from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from .forms import RegistroUsuariaForm

def index(request):
    #if request.method == 'POST':
     #   form = RegistroUsuariaForm(request.POST)
      #  if form.is_valid():
       #     usuaria = form.save(commit=False)
        #    usuaria = Usuaria.objects.create(
         #       identificacion=form.cleaned_data['identificacion'],
          #      nombre=form.cleaned_data['nombre'],
           #     correo=form.cleaned_data['correo'],
            #    contraseña=form.cleaned_data['contraseña'],
             #   tipo=form.cleaned_data['tipo'],
              #  celular=form.cleaned_data['celular'],
               # placa=form.cleaned_data['placa'],
            #)
            
            #usuaria.save()
            #messages.success(request, f'Usuaria {nombre} creada')
            #return redirect('index')
    #else:
     #   form = RegistroUsuariaForm()
    return render(request, 'index.html', {'form'})

def signinCond(request):
    return render(request, "signinCond.html ")