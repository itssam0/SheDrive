from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Usuaria)

admin.site.register(Conductora)

admin.site.register(Carro)

admin.site.register(Viaje)

class UsuariaAdmin(admin.ModelAdmin):
     list_display = ('nombre', 'identificacion', 'celular', 'correo', 'contraseña')
