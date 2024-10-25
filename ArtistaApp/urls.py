from django.contrib import admin
from django.urls import path
from ArtistaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('lista/',views.lista),
    path('agregar/',views.registrarArtista),
    path('eliminarArtista/<int:id>',views.eliminarArtista),
    path('actualizarArtista/<int:id>',views.actualizarArtista)
]