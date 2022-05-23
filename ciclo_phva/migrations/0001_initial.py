# Generated by Django 4.0.4 on 2022-05-23 15:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('porcentaje_maximo', models.FloatField(max_length=45)),
                ('porcentaje_obtenido', models.FloatField(max_length=45)),
                ('calificacion_maxima', models.FloatField(max_length=45)),
                ('calificacion_obtenida', models.FloatField(max_length=45)),
            ],
            options={
                'verbose_name': 'Ciclo',
                'verbose_name_plural': 'Ciclos',
                'db_table': 'ciclo',
            },
        ),
        migrations.CreateModel(
            name='Estandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('porcentaje_maximo', models.FloatField(max_length=45)),
                ('porcentaje_obtenido', models.FloatField(max_length=45)),
                ('calificacion_maxima', models.FloatField(max_length=45)),
                ('calificacion_obtenida', models.FloatField(max_length=45)),
            ],
            options={
                'verbose_name': 'Estandar',
                'verbose_name_plural': 'Estandars',
                'db_table': 'estandar',
            },
        ),
        migrations.CreateModel(
            name='Evidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evidencia', models.CharField(max_length=200)),
                ('formato', models.FileField(upload_to='pdf/', validators=[django.core.validators.FileExtensionValidator(['png', 'pdf'])])),
            ],
            options={
                'verbose_name': 'Evidencia',
                'verbose_name_plural': 'Evidencias',
                'db_table': 'evidencia',
            },
        ),
        migrations.CreateModel(
            name='RegistroAnual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=65)),
            ],
            options={
                'verbose_name': 'RegistroAnual',
                'verbose_name_plural': 'RegistroAnuals',
                'db_table': 'registro_anual',
            },
        ),
        migrations.CreateModel(
            name='ItemEstandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('estado', models.SmallIntegerField(null=True)),
                ('nombre_formato', models.CharField(max_length=200, null=True)),
                ('formato', models.FileField(upload_to='pdf/')),
                ('fk_sub_estandar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.estandar')),
            ],
            options={
                'verbose_name': 'ItemEstandar',
                'verbose_name_plural': 'ItemEstandars',
                'db_table': 'item_estandar',
            },
        ),
    ]
