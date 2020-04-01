# Generated by Django 3.0.4 on 2020-03-19 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicacoes', '0004_auto_20200318_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('caracteristicas', models.TextField(verbose_name='Caracaterísticas')),
                ('data_pub', models.DateTimeField(auto_now=True, verbose_name='Data de Publicação')),
                ('imagem', models.ImageField(upload_to='posts', verbose_name='Imagem')),
                ('estado', models.CharField(choices=[('P', 'Perdido'), ('PA', 'Para Adoção'), ('E', 'Encontrado')], max_length=15, verbose_name='Categoria')),
                ('sexo', models.CharField(choices=[('F', 'Fêmea'), ('M', 'Macho')], max_length=8, verbose_name='Sexo')),
                ('porte', models.CharField(choices=[('PE', 'Pequeno'), ('ME', 'Médio'), ('GR', 'Grande')], max_length=8, verbose_name='Porte')),
                ('vacinado', models.BooleanField(verbose_name='Vacinado')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-data_pub',),
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
