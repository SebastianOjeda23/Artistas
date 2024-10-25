from django.shortcuts import render,redirect
from ArtistaApp.models import Artista
from ArtistaApp.forms import FormArtista

def index(request):
    return render(request,'ArtistaApp/index.html')

def lista(request):
    artistas = Artista.objects.all()
    data = {'artistas' : artistas}
    return render(request,'ArtistaApp/lista.html',data)

def registrarArtista(request):
    form = FormArtista()
    if request.method == 'POST':
        form = FormArtista(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request,'ArtistaApp/registrar.html',data)

def actualizarArtista(request,id):
    artistas = Artista.objects.get(id = id)
    form = FormArtista (instance=artistas)
    if request.method == 'POST':
        form = FormArtista(request.POST , instance=artistas)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,'ArtistaApp/registrar.html',data)


def eliminarArtista(request,id):
    artistas = Artista.objects.get(id = id)
    artistas.delete()
    return redirect('../lista')
# Create your views here.
