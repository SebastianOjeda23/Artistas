from django.contrib import admin
from django.urls import path
from ArtistaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('lista/',views.lista),
    path('agregar/',views.registrarArtista),
    path('eliminarArtista/<int:id>',views.eliminarArtista),
    path('actualizarArtista/<int:id>',views.actualizarArtista),
    path('lista2/',views.listaMusica),
    path('agregaMusica',views.registrarMusica),
    path('actualizaMusica/<int:id>',views.actualizarMusica),
    path('eliminaMusica/<int:id>',views.eliminaMusica),
    path('lista3/',views.listaAlbum),
    path('agregaAlbum/',views.registrarAlbum),
    path('actualizaAlbum/<int:id>',views.actualizaAlbum),
    path('eliminaAlbum/<int:id>',views.eliminarAlbum)
]