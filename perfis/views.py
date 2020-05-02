from django.shortcuts import render, redirect
from publicacoes.models import Animal
from django.contrib.auth.models import User
from users.models import Perfil
from users.forms import UserForm, PerfilForm
from django.contrib.auth.decorators import login_required 

@login_required
def perfil(request):
    animais = Animal.objects.filter(usuario=request.user.id)
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.filter(user=request.user.id).first
    contexto = {
        'animais':animais,
        'usuario':usuario,
        'perfil_usuario':perfil_usuario,
    }
    
    return render(request, 'perfil.html', contexto)

@login_required
def alterar(request, id):
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.get(user=request.user.id)
    form = UserForm(request.POST or None, instance=usuario)
    form_perfil = PerfilForm(request.POST or None, request.FILES or None, 
                            instance=perfil_usuario)
    contexto = {
        'usuario':usuario,
        'perfil_usuario':perfil_usuario,
        'form':form,
        'form_perfil':form_perfil,
    }
    print(form_perfil.is_valid())
    if form_perfil.is_valid():
        edit = form_perfil.save(commit=False)
        edit.save()
        return redirect('informacoes-pessoais')
        
    return render(request,'alterar-informacoes.html', contexto)

@login_required
def informacoes(request):
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.filter(user=request.user.id).first
    contexto = {
        'usuario':usuario,
        'perfil_usuario':perfil_usuario,
    }
    return render(request, 'informacoes-pessoais.html', contexto)

@login_required
def excluir_conta(request, id):
    usuario = User.objects.get(id=id)
    contexto = {
        'usuario':usuario,
    }

    if request.method == 'POST':
        usuario.delete()
        return redirect('/')

    return render(request, 'excluir-conta.html', contexto)

@login_required
def excluir_animal(request, id):
    animal = Animal.objects.get(id=id)
    animal.delete()
    return redirect('animais')