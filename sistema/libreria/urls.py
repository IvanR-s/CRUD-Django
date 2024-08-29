from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos', views.producto, name='productos'),
    path('ventas', views.venta, name='ventas'),
    path('compras', views.compra, name='compras'),
    path('Provedor', views.Provedor, name='Provedor'),
    path('usuario', views.Usuario, name='usuario'),
    path('tablausuario', views.tablausuarios, name='tablausuarios'),
    path('iniciarsesion', views.iniciosesion, name='iniciarsesion'),
    path('crearproducto', views.Crearproducto, name='crearproducto'),
]
