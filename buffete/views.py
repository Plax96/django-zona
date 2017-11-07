from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def listarcasoslibres(request):
    casos=Expediente.objects.filter(fecha_ingreso__lte=timezone.now(),estado='1').order_by('fecha_ingreso')
    return render(request, 'buffete/listarcasoslibres.html',{'casos':casos})

@login_required
def listarcasosllevados(request):
    casos=Expediente.objects.filter(estado='2').order_by('fecha_ingreso')
    return render(request, 'buffete/listarcasosocupados.html',{'casos':casos})

@login_required
def detalle_caso(request,iden):
    caso = get_object_or_404(Expediente, id=iden)
    return render(request, 'buffete/detalle_caso.html',{'caso':caso})

@login_required
def nuevocaso(request):
    if request.method == "POST":
        exp = ExpedienteForm(request.POST)
        if exp.is_valid():
            expediente = exp.save(commit = False)
            expediente.author = request.user
            expediente.save()
            return redirect('detalle_caso', iden=expediente.id)
    else:
        expediente = ExpedienteForm()
    return render(request, 'buffete/caso_editar.html', {'form':expediente})

@login_required
def caso_editar(request, iden):
    post= get_object_or_404(Expediente, id=iden)
    if request.method == "POST":
        exp = ExpedienteForm(request.POST, instance=post)
        if exp.is_valid():
            expediente = exp.save(commit = False)
            if exp.cleaned_data['abogado']:
                expediente.estado="2"
            else:
                expediente.estado="1"
            expediente.author = request.user
            expediente.save()
            return redirect('detalle_caso', iden=expediente.id)
    else:
        expediente = ExpedienteForm(instance=post)
    return render(request, 'buffete/caso_editar.html', {'form':expediente})


@login_required
def eliminar_cliente(request,id):
    cliente= get_object_or_404(Cliente, id=id)
    cliente.update(estado=False)
    return render(request, 'buffete/detalle_caso.html',{'caso':caso})

def nuevousuario(request):
   if request.method == "POST":
       us = UserForm(request.POST)
       if us.is_valid():
           usuario = usuario.save(commit=False)
           usuario.author = request.user
           usuario.save()
           return redirect('usuario_nuevo')
   else:
       usuario = UserForm()
       return render(request, 'buffete/usuario_editar.html',{'form':usuario})

def abogadonuevo(request):
  if request.method == "POST":
      abogado = AbogadoForm(request.POST)
      if abogado.is_valid():
          abogado = abogado.save(commit=False)
          abogado.author = request.user
          abogado.save()
          return redirect('casoslibres')
  else:
      abogado = AbogadoForm()
      return render(request, 'buffete/abogado_editar.html', {'form':abogado})


@login_required
def nuevocliente(request):
    if request.method == "POST":
        cliente = ClienteForm(request.POST)
        if cliente.is_valid():
            cliente = cliente.save(commit=False)
            cliente.author = request.user
            cliente.save()
            return redirect('casoslibres')
    else:
        cliente = ClienteForm()
    return render(request, 'buffete/cliente_editar.html', {'form':cliente})
