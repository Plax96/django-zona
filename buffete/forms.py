from django import forms
from .models import *
from django.contrib.auth.models import User

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ('estado','resumen','descripcion','cliente','abogado','fecha_inicio','fecha_finalizacion')

class AbogadoForm(forms.ModelForm):
    class Meta:
        model = Abogado
        fields = ('usuario','nombre','apellido','dpi','telefono')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','apellido','dpi','telefono')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','username','password')
