# Generated by Django 3.0.4 on 2020-03-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0008_auto_20200319_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='castrado',
            field=models.BooleanField(blank=True, verbose_name='Castrado'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='categoria',
            field=models.CharField(blank=True, choices=[('P', 'Perdido'), ('PA', 'Para Adoção'), ('E', 'Encontrado')], max_length=15, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='porte',
            field=models.CharField(blank=True, choices=[('PE', 'Pequeno'), ('ME', 'Médio'), ('GR', 'Grande')], max_length=8, verbose_name='Porte'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'Fêmea'), ('M', 'Macho')], max_length=8, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='vacinado',
            field=models.BooleanField(blank=True, verbose_name='Vacinado'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='vermifugado',
            field=models.BooleanField(blank=True, verbose_name='Vermifugado'),
        ),
    ]
