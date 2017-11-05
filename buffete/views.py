from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

def listarcasos(request):
    casos=Expediente.objects.filter(fecha_ingreso__lte=timezone.now()).order_by('fecha_ingreso')
    return render(request, 'buffete/listarcasos.html',{'casos':casos})
# Create your views here.
