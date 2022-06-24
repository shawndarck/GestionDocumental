from django.db import models
from django.core.validators import FileExtensionValidator


class PoliticaGestionAmbiental(models.Model):
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name='PoliticaGestionAmbiental'
        verbose_name_plural='PoliticaGestionAmbientals'
        db_table='politica_gestion_ambiental'
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion


class EvidenciaGestionAmbiental(models.Model):
    nombre_evidencia = models.CharField(max_length=200)
    formato = models.FileField(upload_to = "pdf/", validators=[FileExtensionValidator(['png', 'pdf'])])
    fk_gestion_ambiental = models.ForeignKey(PoliticaGestionAmbiental, related_name='item_estandar', null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name='EvidenciaGestionAmbiental'
        verbose_name_plural='EvidenciaGestionAmbientals'
        db_table='evidencia_gestion_ambiental'
        ordering = ['id']

    def __str__(self) -> str:
        return self.nombre_evidencia
