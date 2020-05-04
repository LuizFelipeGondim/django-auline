from django.db import models

class Contato(models.Model):
    nome = models.CharField('Nome(Opcional)', max_length=80, default='Anônimo')
    data_envio = models.DateTimeField('Comentado em', auto_now=True)
    conteudo = models.TextField('Como podemos ajudá-lo?', max_length=300)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('-data_envio',)