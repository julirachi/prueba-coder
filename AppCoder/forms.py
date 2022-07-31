from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    
    
class ProfesorFormulario(forms.Form):
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Email {self.email} - Profesion {self.profession}"

    nombre = forms.CharField(max_length = 40)
    apellido = forms.CharField(max_length = 40)
    email = forms.EmailField()
    profession = forms.CharField(max_length = 40)
