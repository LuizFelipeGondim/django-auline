from django.forms import ModelForm
from .models import Animal, Comentario
from django import forms

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'caracteristicas', 'imagem', 'sexo', 'vacinado', 'vermifugado',
        'categoria', 'castrado', 'cidade', 'rua', 'porte', 'estado']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'caracteristicas': forms.Textarea(attrs={"rows":5, "cols":20}),
            'cidade': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cidade atual do animal'}),
            'rua': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Rua onde foi visto pela última vez'}),
            'estado': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado atual do animal'}),
        }

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']