from django.db import models

# Create your models here.
class RegistroAnual(models.Model):
    descripcion = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        verbose_name='RegistroAnual'
        verbose_name_plural='RegistroAnuals'
        db_table='registro_anual'

class Evidencia(models.Model):
    nombre_evidencia = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.nombre_evidencia

    class Meta:
        verbose_name='Evidencia'
        verbose_name_plural='Evidencias'
        db_table='evidencia'


class Ciclo(models.Model):
    descripcion = models.CharField(max_length=45)
    porcentaje_maximo = models.FloatField(max_length=45)
    porcentaje_obtenido = models.FloatField(max_length=45)
    calificacion_maxima = models.FloatField(max_length=45)
    calificacion_obtenida = models.FloatField(max_length=45)
    fk_registro_anual = models.ForeignKey(RegistroAnual, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        verbose_name='Ciclo'
        verbose_name_plural='Ciclos'
        db_table='ciclo'


class Estandar(models.Model):
    descripcion = models.CharField(max_length=45)
    porcentaje_maximo = models.FloatField(max_length=45)
    porcentaje_obtenido = models.FloatField(max_length=45)
    calificacion_maxima = models.FloatField(max_length=45)
    calificacion_obtenida = models.FloatField(max_length=45)
    fk_ciclo = models.ForeignKey(Ciclo, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        verbose_name='Estandar'
        verbose_name_plural='Estandars'
        db_table='estandar'


class SubEstandar(models.Model):
    descripcion = models.CharField(max_length=45)
    porcentaje_maximo = models.FloatField(max_length=45)
    porcentaje_obtenido = models.FloatField(max_length=45)
    calificacion_maxima = models.FloatField(max_length=45)
    calificacion_obtenida = models.FloatField(max_length=45)
    fk_estandar = models.ForeignKey(Estandar, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        verbose_name='SubEstandar'
        verbose_name_plural='SubEstandars'
        db_table='sub_estandar'


class ItemEstandar(models.Model):
    descripcion = models.CharField(max_length=45)
    porcentaje_maximo = models.FloatField(max_length=45)
    porcentaje_obtenido = models.FloatField(max_length=45)
    calificacion_maxima = models.FloatField(max_length=45)
    calificacion_obtenida = models.FloatField(max_length=45)
    formato = models.CharField(max_length=200)
    fk_sub_estandar = models.ForeignKey(SubEstandar, null=True, on_delete=models.CASCADE)
    evidencias = models.ManyToManyField(Evidencia)

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        verbose_name='ItemEstandar'
        verbose_name_plural='ItemEstandars'
        db_table='item_estandar'
