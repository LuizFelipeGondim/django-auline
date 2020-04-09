from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #@login_required
from users.forms import UserForm, PerfilForm
from django.contrib.auth import login as auth_login, authenticate

def cadastro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form_perfil = PerfilForm(request.POST)

        if form.is_valid() and form_perfil.is_valid():
            user = form.save()

            perfil = form_perfil.save(commit=False)
            perfil.user = user

            perfil.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserForm(request.POST)
        form_perfil = PerfilForm(request.POST)

    contexto = {
        'form':form,
        'form_perfil':form_perfil,
    }

    return render(request, 'cadastro.html', contexto)


def login(request):
    return render(request, 'registration/login.html')