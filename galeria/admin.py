# galeria/admin.py
from django.contrib import admin
from .models import Imagen

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nombre', 'tamaño', 'precio')
