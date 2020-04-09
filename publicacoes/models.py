from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):

    ESTADOS = (
        ('P', 'Perdido'),
        ('PA', 'Para Adoção'),
        ('E', 'Encontrado'),
    )

    SEXO = (
        ('F', 'Fêmea'),
        ('M', 'Macho'),
    )

    PORTE = (
        ('PE', 'Pequeno'),
        ('ME', 'Médio'),
        ('GR', 'Grande'),
    )

    nome = models.CharField('Nome', max_length=50)
    caracteristicas = models.TextField('Caracaterísticas')
    data_pub = models.DateTimeField('Data de Publicação', auto_now=True)
    imagem = models.ImageField('Imagem', upload_to='posts')
    categoria = models.CharField('Categoria', max_length=15, choices=ESTADOS, blank=True)
    sexo = models.CharField('Sexo', max_length=8, choices=SEXO, blank=True)
    porte = models.CharField('Porte', max_length=8, choices=PORTE, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vacinado = models.BooleanField('Vacinado', blank=True)
    vermifugado = models.BooleanField('Vermifugado', blank=True)
    castrado = models.BooleanField('Castrado', blank=True)
    estado = models.CharField('Estado', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    rua = models.CharField('Rua', max_length=70)


    class Meta:
        ordering = ('-data_pub', )

    def __str__(self):
        return self.nome