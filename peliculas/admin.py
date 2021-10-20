from django.contrib import admin
from .models import *

# Register your models here.

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre','Sinopsis','duracion','tamanio','poster')
    search_fields = ('nombre','Sinopsis','duracion','tamanio','poster')

admin.site.register(Pelicula, PeliculaAdmin)
