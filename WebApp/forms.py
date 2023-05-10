from django import forms
from django.contrib.auth.models import User

class RegistroUsuariaForm(forms.Form):
    nombre = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nombre'}))
    identificacion = forms.IntegerField(required=True,label='', widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Núm. Identificación'}))
    celular = forms.IntegerField(required=True,label='', widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Núm. Celular'}))
    correo = forms.EmailField(required=True, label='', widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Correo'}))
    contraseña = forms.CharField(required=True,label='', widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields =['nombre', 'identificacion', 'celular', 'correo', 'contraseña']
       
        
class InicionSesionForm(forms.Form):
    identificacion = forms.IntegerField(required=True,label='', widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Núm. Identificación'}))
    contraseña = forms.CharField(required=True,label='', widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields =['identificacion',  'contraseña']

class RegistroCoductorasForm(forms.Form):
    nombre = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nombre'}))
    identificacion = forms.IntegerField(required=True,label='', widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Núm. Identificación'}))
    celular = forms.IntegerField(required=True,label='', widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Núm. Celular'}))
    correo = forms.EmailField(required=True, label='', widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Correo'}))
    contraseña = forms.CharField(required=True,label='', widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}))
    #placa = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Placa vehiculo'}))