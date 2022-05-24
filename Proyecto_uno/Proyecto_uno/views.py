from django.http import HttpResponse
from django.template import Template,Context

def saludar(request):
    return HttpResponse("MI PRIMER PROYECTO")