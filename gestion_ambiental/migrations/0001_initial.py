# Generated by Django 4.0.4 on 2022-06-24 12:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GestionAmbiental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'PoliticaGestionAmbiental',
                'verbose_name_plural': 'PoliticaGestionAmbientals',
                'db_table': 'politica_gestion_ambiental',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='EvidenciaGestionAmbiental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evidencia', models.CharField(max_length=200)),
                ('formato', models.FileField(upload_to='pdf/', validators=[django.core.validators.FileExtensionValidator(['png', 'pdf'])])),
                ('fk_item_estandar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_estandar', to='gestion_ambiental.gestionambiental')),
            ],
            options={
                'verbose_name': 'EvidenciaGestionAmbiental',
                'verbose_name_plural': 'EvidenciaGestionAmbientals',
                'db_table': 'evidencia_gestion_ambiental',
                'ordering': ['id'],
            },
        ),
    ]
