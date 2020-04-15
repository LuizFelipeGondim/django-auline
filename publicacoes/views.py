from django.shortcuts import render, redirect
from publicacoes.models import Animal
from .forms import AnimalForm

def lista_animal(request):

    lista_de_animais = Animal.objects.all()
    
    contexto = {
        'lista_de_animais': lista_de_animais
    }
    return render(request, 'index.html', contexto)

def cadastro_animal(request):

    form = AnimalForm(request.POST or None, request.FILES)
    
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'cadastro-animal.html', {'form':form})