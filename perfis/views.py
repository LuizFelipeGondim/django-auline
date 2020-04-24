from django.shortcuts import render
from publicacoes.models import Animal



def perfil(request):
    animais = Animal.objects.filter(usuario=request.user.id)

    contexto = {
        'animais':animais
    }
    
    return render(request, 'perfil.html', contexto)