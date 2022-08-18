from ast import Pass
from modulefinder import replacePackageMap
from pdb import post_mortem
from typing import Generic
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate, login as logger
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q
from django.contrib.auth.models import User


#RENDERIZAD
def about_us(request):
    return render(request, 'app_biblioteca/about_us.html')


def encargados(request):
    if request.user.is_authenticated:

        return render(request, 'app_biblioteca/encargados.html')
    else:
        return render(request, 'app_biblioteca/encargados.html')
        

def socios(request):
    if request.user.is_authenticated:
        return render(request, 'app_biblioteca/socios.html')
    else:
        return render(request, 'app_biblioteca/socios.html')



def libros(request):
    if request.user.is_authenticated:
        return render(request, 'app_biblioteca/libros.html')
    else:
        return render(request, 'app_biblioteca/libros.html')


#INGRESO
@login_required
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
            return render(request,"app_biblioteca/inicio.html")
    else:
        form = Encargado_Form()
    return render(request,'app_biblioteca/ingreso_encargados.html',{'formulario':form})

@login_required
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
            return render(request,"app_biblioteca/inicio.html")
    else:
        form = Socio_Form()
    return render(request,'app_biblioteca/ingreso_socios.html', {'formulario':form})

@login_required
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
            return render(request,"app_biblioteca/inicio.html")
    else:
        form = Libro_Form()
    return render(request,'app_biblioteca/ingreso_libros.html', {'formulario':form})

#BUSQUEDA
def busqueda_libro(request):
    return render(request, 'app_biblioteca/resultado_libro.html')

def buscar_libro(request):
    if request.GET['codigo']:
        cod= request.GET['codigo']
        codigo = Libro.objects.filter(codigo=cod) 
        return render(request,'app_biblioteca/buscar_libro.html', {'codigo':codigo})
    else:
        return render(request,'app_biblioteca/resultado_libro.html', {'error':'No se ingreso ningun libro'})

def busqueda_socio(request):
    return render(request, 'app_biblioteca/resultado_socio.html')

def buscar_socio(request):
    if request.GET['num_socio']:
        num_soc= request.GET['num_socio']
        num_socio = Socio.objects.filter(num_socio=num_soc) 
        return render(request,'app_biblioteca/buscar_socio.html', {'num_socio':num_socio})
    else:
        return render(request,'app_biblioteca/resultado_socio.html', {'error':'No se ingreso ningun socio'})

def busqueda_encargado(request):
    return render(request, 'app_biblioteca/resultado_encargado.html')

def buscar_encargado(request):
    if request.GET['codigo']:
        cod= request.GET['codigo']
        codigo = Encargado.objects.filter(codigo=cod) 
        return render(request,'app_biblioteca/buscar_encargado.html', {'codigo':codigo})
    else:
        return render(request,'app_biblioteca/resultado_encargado.html', {'error':'No se ingreso ningun socio'})

#LECTURA
def leer_encargados(request):
    encargados = Encargado.objects.all()
    return render(request, 'app_biblioteca/leer_encargados.html',{'encargados':encargados})

def leer_libros(request):
    libros = Libro.objects.all()
    return render(request, 'app_biblioteca/leer_libros.html',{'libros':libros})

def leer_socios(request):
    socios = Socio.objects.all()
    return render(request, 'app_biblioteca/leer_socios.html',{'socios':socios})

#DELETE
@login_required
def eliminar_encargado(request, codigo_encargado):
    encargado = Encargado.objects.get(codigo=codigo_encargado) #trae por cod.
    encargado.delete()
    encargados = Encargado.objects.all()
    return render(request, 'app_biblioteca/leer_encargados.html',{'encargados':encargados})

@login_required
def eliminar_libro(request, codigo_libro):
    libro = Libro.objects.get(codigo=codigo_libro)
    libro.delete()
    libros = Libro.objects.all()
    return render(request, 'app_biblioteca/leer_libros.html',{'libros':libros})

@login_required
def eliminar_socio(request, num_soc):
    socio = Socio.objects.get(num_socio=num_soc)
    socio.delete()
    socios = Socio.objects.all()
    return render(request, 'app_biblioteca/leer_socios.html',{'socios':socios})

@login_required
def editar_encargado(request, codigo_encargado):
    encargado = Encargado.objects.get(codigo=codigo_encargado)
    if request.method == 'POST':
        form = Encargado_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            encargado.nombre= info['nombre']
            encargado.apellido= info['apellido']
            encargado.codigo= info['codigo']
            encargado.email= info['email']
            encargado.save()
            return render(request, 'app_biblioteca/inicio.html')
    else:
        form = Encargado_Form(initial={'nombre':encargado.nombre, 'apellido':encargado.apellido, 'codigo':encargado.codigo, 'email':encargado.email})

    return render(request, 'app_biblioteca/editar_encargado.html',{'formulario':form,'codigo_encargado':codigo_encargado})

@login_required
def editar_socio(request, num_soc):
    socio = Socio.objects.get(num_socio=num_soc)
    if request.method == 'POST':
        form = Socio_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            socio.nombre = info['nombre']
            socio.apellido = info['apellido']
            socio.num_socio= info['num_socio']
            socio.email= info['email']
            socio.fecha_alta= info['fecha_alta']
            socio.save()
            return render(request, 'app_biblioteca/inicio.html')
    else:
        form = Socio_Form(initial={'nombre':socio.nombre, 'apellido':socio.apellido, 'num_socio':socio.num_socio, 'email':socio.email, 'fecha_alta':socio.fecha_alta})
    return render(request, 'app_biblioteca/editar_socio.html',{'formulario':form,'num_soc':num_soc})

@login_required
def editar_libro(request, codigo_libro):
    libro = Libro.objects.get(codigo=codigo_libro)
    if request.method == 'POST':
        form = Libro_Form(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            libro.titulo = info['titulo']
            libro.autor = info['autor']
            libro.genero = info['genero']
            libro.codigo = info['codigo']
            libro.save()
            return render(request, 'app_biblioteca/inicio.html')
    else:
        
        form = Libro_Form(initial={'titulo':libro.titulo, 'autor':libro.autor, 'genero':libro.genero, 'codigo':libro.codigo})
    return render(request, 'app_biblioteca/editar_libro.html',{'formulario':form,'codigo_libro':codigo_libro})


#Login - Logout
@login_required 
def perfil(request):
    avatares= Avatar.objects.filter(user= request.user.id)
    if avatares.exists():
        return render(request,'app_biblioteca/perfil.html',{"av":avatares.first().imagen.url})

    else:

        return render(request, 'app_biblioteca/perfil_2.html')

@login_required 
def perfil_2(request):
    if request.user.is_authenticated:

        return render(request, 'app_biblioteca/perfil_2.html')
    else:
        return render(request, 'app_biblioteca/perfil_".html')

def inicio(request):
    if request.user.is_authenticated:

        return render(request, 'app_biblioteca/inicio.html')
    else:
        return render(request, 'app_biblioteca/inicio.html')


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usu= form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            usuario=authenticate(username=usu, password=clave)

            if usuario is not None:
                logger(request, usuario)
                return render(request,"app_biblioteca/inicio.html", {'form':form,'mensaje':f"Bienvenid@ {usuario}"})
            else:
                return render(request, "app_biblioteca/login.html", {'form':form,'mensaje':'Error,usuario o clave erroneos'})
        else:
            return render(request, "app_biblioteca/login.html", {'form':form, 'mensaje':f'Formulario invalido'})

    form=AuthenticationForm()
    return render(request, "app_biblioteca/login.html", {'form':form})

class editar_perfil(UpdateView):
    form_class = UserEditForm
    template_name = 'app_biblioteca/editar_perfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"app_biblioteca/inicio.html", {'form':form,'mensaje':f'Usuario Creado: {username}'})
    else:
        form = UserRegisterForm()
    return render(request, 'app_biblioteca/register.html',{'form':form})

# class editar_pass(PasswordChangeForm):
#     form_class = PasswordChangingForm
#     success_url = reverse_lazy('inicio')

@login_required
def editar_pass(request):
    if request.method == 'POST':
        form = PasswordChangingForm(user = request.user , data = request.POST)
        if form.is_valid():
            form.save()
            return render(request,"app_biblioteca/inicio.html", {'form':form,'mensaje':f'Contraseña Modificada'})
    else:
        form = PasswordChangingForm( user = request.user)
    return render(request, 'app_biblioteca/editar_pass.html', {'form':form, 'user':request.user})

#POSTEO
class HomeView(ListView):
    model = Post
    template_name = 'app_biblioteca/social.html'
    ordering = ['-id']
    

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'app_biblioteca/article_detail.html'

class agregar_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app_biblioteca/agregar_post.html'


class editar_post(UpdateView):
    model = Post
    form_class = EditarForm
    template_name = 'app_biblioteca/editar_post.html'


class eliminar_post(DeleteView):
    model = Post
    template_name = 'app_biblioteca/eliminar_post.html'
    success_url = reverse_lazy('social')

#Mensajeria nueva---------------------------------------------


class ListThreads(ListView):
    model = ThreadModel
    template_name = 'app_biblioteca/inbox.html'
    ordering = ['-id']

class CreateThread(CreateView):
      form_class = ThreadForm()
      template_name = 'app_biblioteca/create_thread'


class ListThreads(View):
  def get(self, request, *args, **kwargs):
    threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
    
    context = {
        'threads': threads
  }
    return render(request, 'app_biblioteca/inbox.html', context)





class CreateThread(View):
  def get(self, request, *args, **kwargs):
    form = ThreadForm()
    
    context = {
      'form': form
    }
    return render(request, 'app_biblioteca/create_thread.html', context)

  def post(self, request, *args, **kwargs):
    form = ThreadForm(request.POST)
    username = request.POST.get('username')
    try:
      receiver = User.objects.get(username=username)
      if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
        thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
        return redirect('thread', pk=thread.pk)
      
      if form.is_valid():
        sender_thread = ThreadModel( user=request.user, receiver=receiver)
        sender_thread.save()
        thread_pk = sender_thread.pk
        return redirect('thread', pk=thread_pk)
    except:
      return redirect('create-thread')



class CreateMessage(View):
  def post(self, request, pk, *args, **kwargs):
    thread = ThreadModel.objects.get(pk=pk)
    if thread.receiver == request.user:
      receiver = thread.user
    else:
      receiver = thread.receiver
      
    message = MessageModel(
        thread= thread,
        sender_user= request.user,
        receiver_user= thread.receiver,
        body= request.POST.get('message'),
      )
      
    message.save()
    return redirect('thread', pk=pk)


class ThreadView(View):
  def get(self, request, pk, *args, **kwargs):
    form = MessageForm()
    thread = ThreadModel.objects.get(pk=pk)
    message_list = MessageModel.objects.filter(thread__pk__contains=pk)
    context = {
      'thread': thread,
      'form': form,
      'message_list': message_list
    }
    return render(request, 'app_biblioteca/thread.html', context)


