# Generated by Django 3.0.4 on 2020-03-04 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('data_pub', models.DateTimeField(auto_now=True, verbose_name='Data de Publicação')),
                ('imagem', models.ImageField(upload_to='imagens', verbose_name='Imagem')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
