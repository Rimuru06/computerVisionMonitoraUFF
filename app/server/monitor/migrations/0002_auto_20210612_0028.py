# Generated by Django 3.2.4 on 2021-06-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matricula',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='tipoUser',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]