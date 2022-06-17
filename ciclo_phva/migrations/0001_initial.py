# Generated by Django 4.0.4 on 2022-06-17 21:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EstadoItemEstandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'EstadoItemEstandar',
                'verbose_name_plural': 'EstadoItemEstandars',
                'db_table': 'estado_item_estandar',
                'ordering': ['id'],
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
                ('fk_ciclo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.ciclo')),
            ],
            options={
                'verbose_name': 'Estandar',
                'verbose_name_plural': 'Estandars',
                'db_table': 'estandar',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Formato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300)),
                ('formato_nombre', models.FileField(upload_to='formatos/', validators=[django.core.validators.FileExtensionValidator(['png', 'pdf', 'xlsx', 'xls', 'docx', 'doc'])])),
            ],
            options={
                'verbose_name': 'Formato',
                'verbose_name_plural': 'Formatos',
                'db_table': 'formato',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Phva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('porcentaje_maximo', models.FloatField(max_length=45)),
                ('porcentaje_obtenido', models.FloatField(max_length=45)),
                ('calificacion_maxima', models.FloatField(max_length=45)),
                ('calificacion_obtenida', models.FloatField(max_length=45)),
            ],
            options={
                'verbose_name': 'Phva',
                'verbose_name_plural': 'Phvas',
                'db_table': 'phva',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SubEstandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('porcentaje_maximo', models.FloatField(max_length=45)),
                ('porcentaje_obtenido', models.FloatField(max_length=45)),
                ('calificacion_maxima', models.FloatField(max_length=45)),
                ('calificacion_obtenida', models.FloatField(max_length=45)),
                ('fk_estandar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.estandar')),
            ],
            options={
                'verbose_name': 'SubEstandar',
                'verbose_name_plural': 'SubEstandars',
                'db_table': 'sub_estandar',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ItemEstandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('puntaje_obtenido', models.FloatField(max_length=5, null=True)),
                ('puntaje_maximo', models.FloatField(max_length=5, null=True)),
                ('nombre_formato', models.CharField(max_length=200, null=True)),
                ('formato', models.FileField(upload_to='pdf/')),
                ('fk_estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.estadoitemestandar')),
                ('fk_sub_estandar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.subestandar')),
                ('permisos_usuarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ItemEstandar',
                'verbose_name_plural': 'ItemEstandars',
                'db_table': 'item_estandar',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Evidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evidencia', models.CharField(max_length=200)),
                ('formato', models.FileField(upload_to='pdf/', validators=[django.core.validators.FileExtensionValidator(['png', 'pdf'])])),
                ('fk_item_estandar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_estandar', to='ciclo_phva.itemestandar')),
            ],
            options={
                'verbose_name': 'Evidencia',
                'verbose_name_plural': 'Evidencias',
                'db_table': 'evidencia',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='ciclo',
            name='fk_phva',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.phva'),
        ),
    ]
