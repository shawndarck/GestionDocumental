# Generated by Django 4.0.4 on 2022-05-11 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemestandar',
            name='evidencias',
            field=models.ManyToManyField(to='polls.evidencia'),
        ),
    ]
