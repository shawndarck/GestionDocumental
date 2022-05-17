from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType


class Usuario(AbstractUser):
    es_administrador = models.BooleanField(default=False)
    es_usuario = models.BooleanField(default=False)

    class Meta:
        db_table = 'usuario'

    def get_administrador_profile(self):
        perfil_administrador = None
        if hasattr(self, 'perfiladministrador'):
            perfil_administrador = self.perfiladministrador
        return perfil_administrador

    def get_usuario_profile(self):
        perfil_usuario = None
        if hasattr(self, 'perfilusuario'):
            perfil_usuario = self.perfilusuario
        return perfil_usuario


class UsuarioAdministrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)


class UsuarioNormal(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
