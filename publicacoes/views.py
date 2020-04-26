from django.shortcuts import render, redirect
from publicacoes.models import Animal
from .forms import AnimalForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from users.models import Perfil

def lista_animal(request):
    perfil_usuarios = Perfil.objects.all()
    usuarios = User.objects.all()
    lista_de_animais = Animal.objects.all()
    
    contexto = {
        'lista_de_animais': lista_de_animais,
        'perfil_usuarios':perfil_usuarios,
        'usuarios':usuarios,
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

def perfil_animal(request, id):
    animal = Animal.objects.get(id=id)
    contexto = {
        'animal':animal,
    }
    return render(request, 'perfil-animal.html', contexto) 