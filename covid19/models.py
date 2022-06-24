from django.db import models
from django.forms import CharField


class RegistroAnual(models.Model):
    descripcion = models.CharField(max_length=40)

    class Meta:
        verbose_name='RegistroAnual'
        verbose_name_plural='RegistroAnuals'
        db_table='registro_anual'
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion


class PruebasCovid(models.Model):
    fk_registro_anual = models.ForeignKey(RegistroAnual, null=False, on_delete=models.CASCADE)
    casos_sospechosos = models.IntegerField(null=True, blank=True)
    positivos = models.IntegerField(null=True, blank=True)
    negativos = models.IntegerField(null=True, blank=True)
    sin_prueba = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name='PruebasCovid'
        verbose_name_plural='PruebasCovids'
        db_table='pruebas_covid'
        ordering = ['id']


class Epidemiologia(models.Model):
    fk_registro_anual = models.ForeignKey(RegistroAnual, null=True, on_delete=models.CASCADE)
    casos_sospechosos = models.IntegerField()
    hospitalizados = models.IntegerField()
    sintomaticos_recuperados = models.IntegerField()
    asintomaticos = models.IntegerField()
    fallecidos = models.IntegerField()

    class Meta:
        verbose_name='Epidemiologia'
        verbose_name_plural='Epidemiologia'
        db_table='epidemiologia'
        ordering = ['id']


class IncapacidadesCovid(models.Model):
    fk_registro_anual = models.ForeignKey(RegistroAnual, null=True, on_delete=models.CASCADE)
    casos_positivos_con_incapacidad = models.IntegerField()
    numero_incapacidades = models.IntegerField()
    numero_dias_perdidos_covid = models.IntegerField()
    casos_negativos_sin_prueba_con_incapacidad = models.IntegerField()
    numero_dias_perdidos_sospecha = models.IntegerField()

    class Meta:
        verbose_name='IncapacidadesCovid'
        verbose_name_plural='IncapacidadesCovids'
        db_table='incapacidades_covid'
        ordering = ['id']


class Incidencia(models.Model):
    fk_registro_anual = models.ForeignKey(RegistroAnual, null=True, on_delete=models.CASCADE)
    numero_casos = models.IntegerField()
    numero_trabajadores = models.IntegerField()
    porcentaje_incidencia = models.IntegerField()

    class Meta:
        verbose_name='Incidencia'
        verbose_name_plural='Incidencias'
        db_table='incidencia'
        ordering = ['id']


class TipoCasoSospechoso(models.Model):
    fk_registro_anual = models.ForeignKey(RegistroAnual, null=True, on_delete=models.CASCADE)
    casos_por_sintomas = models.IntegerField()
    contacto_directo = models.IntegerField()
    contacto_indirecto = models.IntegerField()
    antes_de_ingreso_cinte = models.IntegerField()
    otros = models.IntegerField()

    class Meta:
        verbose_name='TipoCasoSospechoso'
        verbose_name_plural='TipoCasoSospechosos'
        db_table='tipo_caso_sospechoso'
        ordering = ['id']


class CasosCliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    registros_anuales = models.ManyToManyField(RegistroAnual, through='CasosAnuales')
    total_casos = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name='CasosCliente'
        verbose_name_plural='CasosClientes'
        db_table='casos_cliente'
        ordering = ['id']

    def __str__(self) -> str:
        return self.nombre_cliente


class CasosAnuales(models.Model):
    fk_anual = models.ForeignKey(RegistroAnual, on_delete=models.CASCADE)
    fk_casos_cliente = models.ForeignKey(CasosCliente, on_delete=models.CASCADE)
    numero_casos = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name='CasosAnuales'
        verbose_name_plural='CasosAnualess'
        db_table='casos_anuales'
        ordering = ['id']