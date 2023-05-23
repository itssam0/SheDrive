from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Usuaria



class UsuariaForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = ''
        self.fields.pop('password')
    
    nombre_usu = forms.CharField(label='Nombre Completo')
    celular = forms.IntegerField(label='Núm. celular')
    
    class Meta:
        model = Usuaria
        fields = ('nombre_usu', 'celular', 'correo', 'contraseña')
        

class RegistroCoductorasForm(forms.Form):
    nombre = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nombre'}))
    identificacion = forms.IntegerField(required=True,label='', widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Núm. Identificación'}))
    celular = forms.IntegerField(required=True,label='', widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Núm. Celular'}))
    correo = forms.EmailField(required=True, label='', widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Correo'}))
    contraseña = forms.CharField(required=True,label='', widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}))
    placa = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Placa vehiculo'}))

class RegistroCarrosForm(forms.Form):
    placa = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Placa vehiculo'}))
    marca = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Marca vehiculo'}))
    modelo = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Modelo vehiculo'}))