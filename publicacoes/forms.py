from django.forms import ModelForm
from .models import Animal, Comentario

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'caracteristicas', 'imagem', 'sexo', 'vacinado', 'vermifugado',
        'categoria', 'castrado', 'cidade', 'rua', 'porte', 'estado'] 

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']