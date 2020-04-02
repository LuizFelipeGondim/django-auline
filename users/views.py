from django.shortcuts import render
from users.forms import UserModelForm

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return login(request)

    return render(request, 'cadastro.html', context)

def login(request):
    form = LoginModelForm(request.POST or None)
    context = {'form':form}