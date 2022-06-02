from django.db import models
from usuarios.models import Usuario
from django.core.validators import FileExtensionValidator


class Formato(models.Model):
    descripcion = models.CharField(max_length=300)
    formato_nombre = models.FileField(upload_to = "formatos/", validators=[FileExtensionValidator(['png', 'pdf', 'xlsx', 'xls', 'docx', 'doc'])])

    class Meta:
        verbose_name='Formato'
        verbose_name_plural='Formatos'
        db_table='formato'

    def __str__(self) -> str:
        return self.descripcion


class RegistroAnual(models.Model):
    descripcion = models.CharField(max_length=65)

    class Meta:
        verbose_name='RegistroAnual'
        verbose_name_plural='RegistroAnuals'
        db_table='registro_anual'

    def __str__(self) -> str:
        return self.descripcion


class Phva(models.Model):
    descripcion = models.CharField(max_length=100)
    porcentaje_maximo = models.FloatField(max_length=45)
    porcentaje_obtenido = models.FloatField(max_length=45)
    calificacion_maxima = models.FloatField(max_length=45)
    calificacion_obtenida = models.FloatField(max_length=45)

    class Meta:
        verbose_name='Phva'
        verbose_name_plural='Phvas'
        db_table='phva'

    def __str__(self) -> str:
        return self.descripcion


class Ciclo(models.Model):
    descripcion = models.CharField(max_length=100)
    porcentaje_maximo = models.FloatField(max_length=45)
    porcentaje_obtenido = models.FloatField(max_length=45)
    calificacion_maxima = models.FloatField(max_length=45)
    calificacion_obtenida = models.FloatField(max_length=45)
    fk_phva = models.ForeignKey(Phva, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Ciclo'
        verbose_name_plural='Ciclos'
        db_table='ciclo'

    def __str__(self) -> str:
        return self.descripcion


class Estandar(models.Model):
    descripcion = models.CharField(max_length=200)
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

    def __str__(self) -> str:
        return self.descripcion


class SubEstandar(models.Model):
    descripcion = models.CharField(max_length=200)
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

    def __str__(self) -> str:
        return self.descripcion


class EstadoItemEstandar(models.Model):
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name='EstadoItemEstandar'
        verbose_name_plural='EstadoItemEstandars'
        db_table='estado_item_estandar'

    def __str__(self) -> str:
        return self.descripcion


class ItemEstandar(models.Model):
    descripcion = models.CharField(max_length=200)
    puntaje_obtenido = models.FloatField(null=True, max_length=5)
    puntaje_maximo = models.FloatField(null=True, max_length=5)
    nombre_formato = models.CharField(max_length=200, null=True)
    formato = models.FileField(upload_to = "pdf/")
    fk_sub_estandar = models.ForeignKey(SubEstandar, null=True, on_delete=models.CASCADE)
    fk_estado = models.ForeignKey(EstadoItemEstandar, null=True, on_delete=models.CASCADE)
    permisos_usuarios = models.ManyToManyField(Usuario)

    class Meta:
        verbose_name='ItemEstandar'
        verbose_name_plural='ItemEstandars'
        db_table='item_estandar'

    def __str__(self) -> str:
        return self.descripcion


class Evidencia(models.Model):
    nombre_evidencia = models.CharField(max_length=200)
    formato = models.FileField(upload_to = "pdf/", validators=[FileExtensionValidator(['png', 'pdf'])])
    fk_item_estandar = models.ForeignKey(ItemEstandar, related_name='item_estandar', null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name='Evidencia'
        verbose_name_plural='Evidencias'
        db_table='evidencia'

    def __str__(self) -> str:
        return self.nombre_evidencia
