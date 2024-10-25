from django.contrib import admin
from ArtistaApp.models import Artista

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['nombre_artista','nacionalidad','fechanacimiento','cancionescreada','aniosactivo']

admin.site.register(Artista,ArtistaAdmin)
# Register your models here.
