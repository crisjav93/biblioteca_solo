from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def inicio(request):
    return render(request, 'app_biblioteca/inicio.html')

def encargados(request):
    return render(request, 'app_biblioteca/encargados.html')

def socios(request):
    return render(request, 'app_biblioteca/socios.html')

def libros(request):
    return render(request, 'app_biblioteca/libros.html')

def ingreso_encargados(request):
    if (request.method == 'POST'):
        form = Encargado_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            codigo = info['codigo']
            email = info['email']
            encargado = Encargado(nombre=nombre, apellido=apellido,codigo=codigo,email=email)
            encargado.save()
            return render(request, 'app_biblioteca/inicio.html')
    else:
        form = Encargado_Form()
    return render(request,'app_biblioteca/ingreso_encargados.html',{'formulario':form})

def ingreso_socios(request):
    if (request.method == 'POST'):
        form = Socio_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            num_socio = info['num_socio']
            email = info['email']
            fecha_alta = info['fecha_alta']
            socio = Socio(nombre=nombre, apellido=apellido, num_socio=num_socio, email=email, fecha_alta=fecha_alta)
            socio.save()
            return render(request,'app_biblioteca/inicio.html')
    else:
        form = Socio_Form()
    return render(request,'app_biblioteca/ingreso_socios.html', {'formulario':form})

def ingreso_libros(request):
    if (request.method == 'POST'):
        form = Libro_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            titulo = info['titulo']
            autor = info['autor']
            genero = info['genero']
            codigo = info['codigo']
            libro = Libro(titulo=titulo, autor=autor, genero=genero, codigo=codigo)
            libro.save()
            return render(request,'app_biblioteca/inicio.html')
    else:
        form = Libro_Form()
    return render(request,'app_biblioteca/ingreso_libros.html', {'formulario':form})

def busqueda_libro(request):
    return render(request, 'app_biblioteca/buscar_libro.html')

def buscar_libro(request):
    if request.GET['codigo']:
        cod= request.GET['codigo']
        codigo = Libro.objects.filter(codigo=cod) 
        return render(request,'app_biblioteca/resultado_libro.html', {'codigo':codigo})
    else:
        return render(request,'app_biblioteca/buscar_libro.html', {'error':'No se ingreso ninguna comision'})





