from django.shortcuts import render, redirect
from publicacoes.models import Animal
from .forms import AnimalForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 

def lista_animal(request):

    lista_de_animais = Animal.objects.all()
    
    contexto = {
        'lista_de_animais': lista_de_animais
    }
    return render(request, 'index.html', contexto)

@login_required
def cadastro_animal(request):

    form = AnimalForm(request.POST or None, request.FILES)
    id_user = request.user.id

    if form.is_valid():
        user = User.objects.get(id=request.user.id)
        animal = form.save(commit=False)
        animal.usuario = user
        animal.save()
        return redirect('/')

    return render(request, 'cadastro-animal.html', {'form':form})