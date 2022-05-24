from django.http import HttpResponse
from django.shortcuts import render
from app_mvt.models import familia
from django.template import loader
# Create your views here.

def inicio(request):
    return render (request,"index.html")

#listado de familia
def flia(request):
    flia=familia.objects.all()
    datos={"Datos" : flia}
    return render(request,"lista_flia.html",datos)

#Cargar un familiar
def alta_flia(request):
    familiar= familia(nombre="Marcela", nacimiento="1984-01-26",edad=38,parentesco="tia")
    familiar.save()
    familiar= familia(nombre="Carmen", nacimiento="1959-08-23",edad=63,parentesco="abuela")
    familiar.save()
    familiar= familia(nombre="Mario", nacimiento="1995-03-07",edad=27,parentesco="tio")
    familiar.save()
    texto= "Se guardo en la BD los tres familiares"
    return HttpResponse(texto)