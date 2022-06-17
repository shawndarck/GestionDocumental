# Generated by Django 4.0.4 on 2022-06-17 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciclo_phva', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RegistroAnual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'RegistroAnual',
                'verbose_name_plural': 'RegistroAnuals',
                'db_table': 'registro_anual',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoCasoSospechoso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casos_por_sintomas', models.IntegerField()),
                ('contacto_directo', models.IntegerField()),
                ('contacto_indireto', models.IntegerField()),
                ('antes_de_ingreso_cinte', models.IntegerField()),
                ('otros', models.IntegerField()),
                ('fk_registro_anual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.registroanual')),
            ],
            options={
                'verbose_name': 'TipoCasoSospechoso',
                'verbose_name_plural': 'TipoCasoSospechosos',
                'db_table': 'tipo_caso_sospechoso',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PruebasCovid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casos_sospechosos', models.IntegerField()),
                ('positivos', models.IntegerField()),
                ('negativos', models.IntegerField()),
                ('sin_prueba', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fk_registro_anual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.registroanual')),
            ],
            options={
                'verbose_name': 'PruebasCovid',
                'verbose_name_plural': 'PruebasCovids',
                'db_table': 'pruebas_covid',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_casos', models.IntegerField()),
                ('numero_trabajadores', models.IntegerField()),
                ('porcentaje_incidencia', models.IntegerField()),
                ('fk_registro_anual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.registroanual')),
            ],
            options={
                'verbose_name': 'Incidencia',
                'verbose_name_plural': 'Incidencias',
                'db_table': 'incidencia',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='IncapacidadesCovid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casos_positivos_con_incapacidad', models.IntegerField()),
                ('numero_dias_perdidos_covid', models.IntegerField()),
                ('casos_negativos_sin_prueba_con_incapacidad', models.IntegerField()),
                ('numero_incapacidades', models.IntegerField()),
                ('numero_dias_perdidos_sospecha', models.IntegerField()),
                ('fk_registro_anual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.registroanual')),
            ],
            options={
                'verbose_name': 'IncapacidadesCovid',
                'verbose_name_plural': 'IncapacidadesCovids',
                'db_table': 'incapacidades_covid',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Epidemologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casos_sospechosos', models.IntegerField()),
                ('hospitalizados', models.IntegerField()),
                ('sintomaticos_recuperados', models.IntegerField()),
                ('asintomaticos', models.IntegerField()),
                ('fallecidos', models.IntegerField()),
                ('fk_registro_anual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.registroanual')),
            ],
            options={
                'verbose_name': 'CasosSospechosos',
                'verbose_name_plural': 'CasosSospechosos',
                'db_table': 'casos_sospechosos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CasosCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_casos', models.IntegerField()),
                ('total_casos', models.IntegerField()),
                ('fk_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.cliente')),
                ('fk_registro_anual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ciclo_phva.registroanual')),
            ],
            options={
                'verbose_name': 'CasosCliente',
                'verbose_name_plural': 'CasosClientes',
                'db_table': 'casos_cliente',
                'ordering': ['id'],
            },
        ),
    ]
