from django.forms import ModelForm
from .models import Contato
from django import forms 

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = {'nome', 'email', 'conteudo'}
        