from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuariaForm(UserCreationForm): 
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nombre'}))
    identificacion = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Núm. Identificación'}))
    celular = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Núm. Celular'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Correo'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields =['nombre', 'identificacion', 'celular', 'correo', 'contraseña']
        help_texts = {k:"" for k in fields}
