from django.urls import path
from .views import *


urlpatterns = [

    path('inicio/', inicio, name='inicio'),
    path('encargados/', encargados, name='encargados'),
    path('socios/',socios, name='socios'),
    path('libros/',libros,name='libros'),
    path('ingreso_encargados/',ingreso_encargados, name='ingreso_encargados'),
    path('ingreso_socios/', ingreso_socios, name = 'ingreso_socios'),
    path('ingreso_libros/', ingreso_libros, name='ingreso_libros'),
    path('buscar_libro/', busqueda_libro, name = 'buscar_libro'),
    path('resultado_libro/', buscar_libro, name='resultado_libro'),
        
]