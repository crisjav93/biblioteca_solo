from django import forms

class Encargado_Form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    codigo = forms.IntegerField()
    email = forms.CharField()

class Socio_Form(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    num_socio=forms.IntegerField()
    email=forms.EmailField()
    fecha_alta=forms.DateField()

class Libro_Form(forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=50)
    codigo =forms.IntegerField()