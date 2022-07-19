from django.contrib import admin
from .views import *
from .models import *

admin.site.register(Encargado)
admin.site.register(Socio)
admin.site.register(Libro)

# Register your models here.
