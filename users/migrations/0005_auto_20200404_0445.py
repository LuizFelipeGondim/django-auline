# Generated by Django 3.0.4 on 2020-04-04 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_perfil_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='data_de_nascimento',
            field=models.DateField(max_length=10, verbose_name='Data de nascimento'),
        ),
    ]
