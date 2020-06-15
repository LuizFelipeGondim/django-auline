from django.forms import ModelForm
from .models import Contato
from django import forms 

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = {'nome', 'email', 'conteudo'}
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'conteudo': forms.Textarea(attrs={'class':'form-control', "rows":5, "cols":20}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adicione um E-mail válido'}),
        }
        