from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def listarcasos(request):
    casos=Expediente.objects.filter(fecha_ingreso__lte=timezone.now(),estado='1').order_by('fecha_ingreso')
    return render(request, 'buffete/listarcasos.html',{'casos':casos})

@login_required
def detallecaso(request,id):
    caso = get_object_or_404(Expediente, id=id)
    return render(request, 'buffete/detalle_caso.html',{'caso':caso})

@login_required
def nuevocaso(request):
    expediente = ExpedienteForm()
    return render(request, 'buffete/caso_editar.html', {'form':expediente})

@login_required
def eliminar_cliente(request,id):
    cliente= get_object_or_404(Cliente, id=id)
    cliente.update(estado=False)
    return render(request, 'buffete/detalle_caso.html',{'caso':caso})

def nuevousuario(request):
   if request.method == "POST":
       usuario = UserForm(request.POST)
       if form.is_valid():
           usuario = usuario.save(commit=False)
           usuario.author = request.user
           usuario.save()
           return redirect('abogado_nuevo')
   else:
       usuario = UserForm()
       return render(request, 'buffete/abogado_nuevo.html', {'form':usuario})

def abogadonuevo(request):
  if request.method == "POST":
      abogado = AbogadoForm(request.POST)
      if form.is_valid():
          abogado = abogado.save(commit=False)
          abogado.author = request.user
          abogado.save()
          return redirect('listarcasos')
  else:
      usuario = AbogadoForm()
      return render(request, 'buffete/listarcasos.html', {'form':usuario})


@login_required
def nuevocliente(request):
    if request.method == "POST":
        cliente = ClienteForm(request.POST)
        if form.is_valid():
            cliente = cliente.save(commit=False)
            cliente.author = request.user
            cliente.save()
            return redirect('listarcasos')
    else:
        cliente = ClienteForm()
    return render(request, 'buffete/cliente_editar.html', {'form':cliente})
