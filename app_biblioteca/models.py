from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, date

# Create your models here.
class Encargado(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    codigo=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.nombre+' '+self.apellido+' '+str(self.codigo)+' '+self.email

class Socio(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    num_socio=models.IntegerField()
    email=models.EmailField()
    fecha_alta=models.DateField()

    def __str__(self):
        return self.nombre+' '+self.apellido+' '+str(self.num_socio)+' '+self.email+' '+str(self.fecha_alta)

class Libro(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    codigo=models.IntegerField()

    def __str__(self):
        return self.titulo+' '+self.autor+' '+self.genero+' '+str(self.codigo)

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank= True)

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    fecha_post = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + ' - Autor: ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('social')


#Mensajeria---------------------------------





class ThreadModel(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  has_unread = models.BooleanField(default=False)

class MessageModel(models.Model):
  thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
  sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  body = models.CharField(max_length=1000)
  image = models.ImageField(upload_to='', blank=True, null=True)
  date = models.DateTimeField(default=timezone.now)
  is_read = models.BooleanField(default=False)