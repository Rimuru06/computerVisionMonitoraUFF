# Generated by Django 3.2.4 on 2021-06-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20210612_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matricula',
            field=models.CharField(blank=True, max_length=150, verbose_name='Matricula'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tipoUser',
            field=models.CharField(blank=True, max_length=150, verbose_name='Função'),
        ),
    ]
