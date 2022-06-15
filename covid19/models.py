from django.db import models

# Create your models here.
class RegistroAnual(models.Model):
    descripcion = models.CharField(max_length=65)

    class Meta:
        verbose_name='RegistroAnual'
        verbose_name_plural='RegistroAnuals'
        db_table='registro_anual'
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion


class PruebasCovid(models.Model):
    fk_registro_anual = models.ForeignKey(RegistroAnual, null=True, on_delete=models.CASCADE)
    casos_sospechosos = models.IntegerField(max_length=45)
    positivos = models.IntegerField(max_length=45)
    negativos = models.IntegerField(max_length=45)
    sin_prueba = models.IntegerField(max_length=45)
    total = models.IntegerField(max_length=45)

    class Meta:
        verbose_name='PruebasCovid'
        verbose_name_plural='PruebasCovids'
        db_table='pruebas_covid'
        ordering = ['id']


class CasosSospechosos(models.Model):
    fk_registro_anual = models.ForeignKey(RegistroAnual, null=True, on_delete=models.CASCADE)
    casos_sospechosos = models.IntegerField(max_length=45)
    hospitalizados = models.IntegerField(max_length=45)
    sintomaticos_recuperados = models.IntegerField(max_length=45)
    asintomaticos = models.IntegerField(max_length=45)
    fallecidos = models.IntegerField(max_length=45)

    class Meta:
        verbose_name='CasosSospechosos'
        verbose_name_plural='CasosSospechosos'
        db_table='casos_sospechosos'
        ordering = ['id']


class IncapacidadesCovid(models.Model):
    fk_registro_anual = models.ForeignKey(RegistroAnual, null=True, on_delete=models.CASCADE)
    casos_positivos_con_incapacidad = models.IntegerField(max_length=45)
    numero_incapacidades = models.IntegerField(max_length=45)
    numero_dias_perdidos_covid = models.IntegerField(max_length=45)

    class Meta:
        verbose_name='IncapacidadesCovid'
        verbose_name_plural='IncapacidadesCovids'
        db_table='incapacidades_covid'
        ordering = ['id']


