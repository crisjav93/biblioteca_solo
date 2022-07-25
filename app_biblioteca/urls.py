from django.urls import path
from .views import *


urlpatterns = [

    path('', inicio, name='inicio'),
    path('encargados/', encargados, name='encargados'),
    path('socios/',socios, name='socios'),
    path('libros/',libros,name='libros'),
    path('ingreso_encargados/',ingreso_encargados, name='ingreso_encargados'),
    path('ingreso_socios/', ingreso_socios, name = 'ingreso_socios'),
    path('ingreso_libros/', ingreso_libros, name='ingreso_libros'),
    path('buscar_libro/', busqueda_libro, name = 'buscar_libro'),
    path('resultado_libro/', buscar_libro, name='resultado_libro'),
    path('buscar_socio/', busqueda_socio, name = 'buscar_socio'),
    path('resultado_socio/', buscar_socio, name='resultado_socio'),
    path('buscar_encargado/', busqueda_encargado, name = 'buscar_encargado'),
    path('resultado_encargado/', buscar_encargado, name='resultado_encargado'),
    path('leer_encargados/',leer_encargados, name='leer_encargados'),
    path('leer_libros/', leer_libros, name='leer_libros'),
    path('leer_socios/', leer_socios, name = 'leer_socios'),
    path('eliminar_encargado/<codigo_encargado>', eliminar_encargado, name='eliminar_encargado'),
    path('eliminar_libro/<codigo_libro>', eliminar_libro, name='eliminar_libro'),
    path('eliminar_socio/<num_soc>', eliminar_socio, name='eliminar_socio'),

]