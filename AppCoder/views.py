from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoFormulario,ProfesorFormulario


# Create your views here.
def curso(self):
    
    curso= Curso(nombre='Python', camada = 23800)
    curso.save()
    texto = f' ---> Curso: {curso.nombre}   Camada: {curso.camada}'
    return HttpResponse(texto)

def inicio(request):
    return  render(request, 'AppCoder/inicio.html')

def cursos(request):
    return  render(request, 'AppCoder/cursos.html')

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apelllido = informacion['apellido'], email = informacion['email'],profesion = informacion['profesion'])
            profesor.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ProfesorFormulario()
        
    return render(request, 'AppCoder/profesores.html',{"miFormulario":miFormulario})


def estudiantes(request):
    return  render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return  render(request, 'AppCoder/entregables.html')

def cursos(request):
    
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada = informacion['camada'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()
        
    return render(request, 'AppCoder/cursos.html',{"miFormulario":miFormulario})

def busquedaCamada(request):
    
    return render(request,"AppCoder/busquedaCamada.html")

def buscar(request):
    
    
    if request.GET['camada']:
        
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] } "
        camada = request.GET['camada']
        cursos = Curso.objetct.filter(camada__icontains=camada)
        return render(request, 'AppCoder/resultadosBusqueda.html', {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "AppCoder/leerProfesores.html",contexto)

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    profesores = Profesor.objects.all()
    
    contexto = {"profesores":profesores}
    
    return render(request,"AppCoder/leerProfesores.html",contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellidp = informacion['apellidp']
            profesor.email = informacion['email']
            profesor.profession = informacion['profession']
            profesor.save()
            return render(request, 'AppCoder/leerProfesores.html')
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre,'apellido':profesor.apellido, 'email':profesor.email,'profesion':profesor.profesion})
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre": profesor_nombre})       