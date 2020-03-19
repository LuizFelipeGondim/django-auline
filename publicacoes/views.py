from django.shortcuts import render
from publicacoes.models import Post

def lista_pub(request):

    lista_de_posts = Post.objects.all()
    
    contexto = {
        'lista_de_posts': lista_de_posts
    }
    return render(request, 'index.html', contexto)
