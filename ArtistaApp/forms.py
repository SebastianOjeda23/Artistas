from django import forms
from ArtistaApp.models import Artista

class FormArtista(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'


    def clean_cancionescreada(self):
        cancionescreada = self.cleaned_data.get('cancionescreada')
        if cancionescreada < 0:
            raise forms.ValidationError("El número de canciones creadas no puede ser negativo.")
        return cancionescreada
    
    def clean_aniosactivo(self):
        aniosactivo = self.cleaned_data.get('aniosactivo')
        if aniosactivo < 0:
            raise forms.ValidationError("El número de años activo no puede ser negativo.")
        return aniosactivo