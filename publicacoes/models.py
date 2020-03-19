from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    nome = models.CharField('Nome', max_length=50)
    conteudo = models.TextField('Conteúdo')
    data_pub = models.DateTimeField('Data de Publicação', auto_now=True)
    imagem = models.ImageField('Imagem', upload_to='posts')

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome