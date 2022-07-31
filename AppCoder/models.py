from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length = 40)
    camada = models.IntegerField()

class Estudiante(models.Model):

    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()

class Profesor(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Email {self.email} - Profesion {self.profession}"

    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField()
    profession = models.CharField(max_length = 40)
    

class Entregable(models.Model):

    nombre = models.CharField(max_length = 40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()