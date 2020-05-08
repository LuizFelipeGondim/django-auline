from django.shortcuts import render, redirect
from .models import Animal, Comentario
from .forms import AnimalForm, ComentarioForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from users.models import Perfil

def lista_animal(request):
    categorias = {}
    ids = []
    perfil_usuarios = Perfil.objects.all()
    usuarios = User.objects.all()
    lista_de_animais = Animal.objects.all()

    for animal in lista_de_animais:
        categorias[animal.id] = animal.categoria
        ids.append(animal.id)
    
    contexto = {
        'lista_de_animais': lista_de_animais,
        'perfil_usuarios':perfil_usuarios,
        'usuarios':usuarios,
        'categorias': categorias,
        'ids': ids,
    }
    return render(request, 'index.html', contexto)

@login_required
def cadastro_animal(request):

    form = AnimalForm(request.POST or None, request.FILES)
    id_user = request.user.id

    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            animal = form.save(commit=False)
            animal.usuario = user
            animal.save()
            return redirect('/')

    return render(request, 'cadastro-animal.html', {'form':form})

def perfil_animal(request, id):
    animal = Animal.objects.get(id=id)
    comentarios = Comentario.objects.filter(animal_id=animal.id)
    form = ComentarioForm(request.POST or None)
    contexto = {
        'animal':animal,
        'form':form,
        'comentarios':comentarios,
    }
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            user_profile = Perfil.objects.get(user=request.user.id)
            comentario = form.save(commit=False)
            comentario.animal = animal
            comentario.avatar = user_profile.foto
            comentario.autor = user.username
            comentario.save()
            return redirect('/')
    
    return render(request, 'perfil-animal.html', contexto) 