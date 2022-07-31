from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso


# Create your views here.
def curso(self):
    
    curso= Curso(nombre='Python', camada = 23800)
    curso.save()
    texto = f' ---> Curso: {curso.nombre}   Camada: {curso.camada}'
    return HttpResponse(texto)