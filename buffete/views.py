from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import *

def listarcasos(request):
    casos=Expediente.objects.filter(fecha_ingreso__lte=timezone.now(),estado='1').order_by('fecha_ingreso')
    return render(request, 'buffete/listarcasos.html',{'casos':casos})

def detallecaso(request,id):
    caso = get_object_or_404(Expediente, id=id)
    return render(request, 'buffete/detalle_caso.html',{'caso':caso})
