from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyectos, Habilidades, Servicios

# Create your views here.
def Index(request):
    habilidades = Habilidades.objects.all()
    servicios = Servicios.objects.all()
    proyectos = Proyectos.objects.all()
    return render(request,'index.html', {
        'habilidades' : habilidades,
        'servicios' : servicios,
        'proyectos' : proyectos
    })