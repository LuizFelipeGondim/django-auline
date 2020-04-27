from django.shortcuts import render, redirect
from publicacoes.models import Animal
from django.contrib.auth.models import User
from users.models import Perfil
from users.forms import UserForm, PerfilForm


def perfil(request):
    animais = Animal.objects.filter(usuario=request.user.id)
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.filter(user=request.user.id).first
    print(usuario.email)
    contexto = {
        'animais':animais,
        'usuario':usuario,
        'perfil_usuario':perfil_usuario,
    }
    
    return render(request, 'perfil.html', contexto)

def alterar(request, id):
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.get(user=request.user.id)
    form = UserForm(request.POST or None, instance=usuario)
    form_perfil = PerfilForm(request.POST or None, instance=perfil_usuario)
    contexto = {
        'usuario':usuario,
        'perfil_usuario':perfil_usuario,
        'form':form,
        'form_perfil':form_perfil,
    }
    if form.is_valid:
        form.save()
        form_perfil.save()
        return redirect('informacoes-pessoais')
        
    return render(request,'alterar-informacoes.html', contexto)

def informacoes(request):
    usuario = User.objects.get(id=request.user.id)
    perfil_usuario = Perfil.objects.filter(user=request.user.id).first
    print(usuario.email)
    contexto = {
        'usuario':usuario,
        'perfil_usuario':perfil_usuario,
    }
    return render(request, 'informacoes-pessoais.html', contexto)

def excluir_conta(request, id):
    usuario = User.objects.get(id=id)
    contexto = {
        'usuario':usuario,
    }

    if request.method == 'POST':
        usuario.delete()
        return redirect('/')

    return render(request, 'excluir-conta.html', contexto)