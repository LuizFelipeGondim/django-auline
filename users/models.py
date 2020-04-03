from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.CharField('Endereço', max_length=30, blank=True)
    data_de_nascimento = models.DateField('Data de nascimento', null=True, blank=True, auto_now=True)
    telefone = models.CharField('Telefone', max_length=15)
    foto = models.ImageField('Foto de Perfil', upload_to='perfil')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()

