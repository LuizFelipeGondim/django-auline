from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_de_nascimento = models.DateField('Data de nascimento', max_length=10)
    telefone = models.CharField('Telefone para contato', max_length=15)
    foto = models.ImageField('Foto de Perfil', upload_to='perfil', default='perfil/unknow.png')
    estado_usuario = models.CharField('Estado', max_length=50)
    cidade_usuario = models.CharField('Cidade', max_length=50, blank=True)
    rua_usuario = models.CharField('Rua', max_length=70, blank=True)

    def __str__(self):
        return self.user.username



