from django.shortcuts import render

def listarcasos(request):
    return render(request, 'buffete/listarcasos.html',{})
# Create your views here.
