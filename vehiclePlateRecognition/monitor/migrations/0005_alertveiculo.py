# Generated by Django 3.2.4 on 2021-06-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_auto_20210615_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertVeiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('license_plate', models.CharField(max_length=7)),
                ('motivo', models.TextField(blank=True, max_length=400)),
            ],
        ),
    ]