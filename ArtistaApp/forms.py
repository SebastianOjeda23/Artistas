from django import forms
from ArtistaApp.models import Artista

class FormArtista(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'
