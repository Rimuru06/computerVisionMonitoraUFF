# Generated by Django 4.0.2 on 2022-06-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicodeteccaoface',
            name='monitor',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
