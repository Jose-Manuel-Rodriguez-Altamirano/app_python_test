# galeria/views.py

from django.shortcuts import render
from .models import Imagen

def index(request):
    imagenes = Imagen.objects.all()[:8]
    return render(request, 'galeria/index.html', {'imagenes': imagenes})

