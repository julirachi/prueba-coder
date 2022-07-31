from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="cursoFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/',views.buscar),
    path('leerProfesores', views.leerProfesores, name="leerProfesores"),
    path('eliminarProfesor', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor', views.editarProfesor, name="EditarProfesor"),
]