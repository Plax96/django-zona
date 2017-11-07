from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listarcasoslibres,name="casoslibres"),
    url(r'^casos/ocupados$', views.listarcasosllevados,name="casosocupados"),
    url(r'^caso/terminar$', views.terminar_caso,name="terminar_caso"),
    url(r'^casos/terminados$', views.listarcasosterminados,name="casosterminados "),
    url(r'^caso/(?P<iden>\d+)/$', views.detalle_caso, name="detalle_caso"),
    url(r'^caso/nuevo/$', views.nuevocaso, name="nuevo_caso"),
    url(r'^caso/editar/(?P<iden>\d+)/$', views.caso_editar, name='caso_editar'),
    url(r'^cliente/nuevo/$', views.nuevocliente, name="nuevo_cliente"),
    url(r'^usuario/nuevo/$', views.nuevousuario, name="usuario_nuevo"),
    url(r'^abogado/nuevo/$', views.abogadonuevo, name="abogado_nuevo"),

    ]
