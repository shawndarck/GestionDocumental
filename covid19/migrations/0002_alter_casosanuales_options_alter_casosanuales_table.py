# Generated by Django 4.0.4 on 2022-06-23 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casosanuales',
            options={'ordering': ['id'], 'verbose_name': 'CasosAnuales', 'verbose_name_plural': 'CasosAnualess'},
        ),
        migrations.AlterModelTable(
            name='casosanuales',
            table='casos_anuales',
        ),
    ]
