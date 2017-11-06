from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listarcasos,name="casos"),
    url(r'^caso/(?P<id>\d+)/$', views.detallecaso, name="detalle_caso"),
    url(r'^caso/nuevo/$', views.nuevocaso, name="nuevo_caso"),
    url(r'^cliente/nuevo/$', views.nuevocliente, name="nuevo_cliente"),
    url(r'^usuario/nuevo/$', views.nuevousuario, name="usuario_nuevo"),
    url(r'^abogado/nuevo/$', views.abogadonuevo, name="abogado_nuevo"),
    ]
