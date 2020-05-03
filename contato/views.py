from django.shortcuts import render, redirect
from .forms import ContatoForm

def contato(request):
    form = ContatoForm(request.POST or None)

    contexto = {
        'form':form
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'entre-em-contato.html', contexto)