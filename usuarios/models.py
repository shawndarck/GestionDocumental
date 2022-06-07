from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group



class Usuario(AbstractUser):
    es_administrador = models.BooleanField(default=False)
    es_usuario = models.BooleanField(default=False)
    es_gestor = models.BooleanField(default=False)
    es_valido = models.BooleanField(default=False)

    class Meta:
        db_table = 'usuario'


    def get_administrador_profile(self):
        perfil_administrador = None
        if hasattr(self, 'perfiladministrador'):
            perfil_administrador = self.perfiladministrador
        return perfil_administrador


    def get_gestor_profile(self):
        perfil_gestor = None
        if hasattr(self, 'perfilgestor'):
            perfil_gestor = self.perfilgestor
        return perfil_gestor


    def get_normal_profile(self):
        perfil_normal = None
        if hasattr(self, 'perfilnormal'):
            perfil_normal = self.perfil_normal
        return perfil_normal

    # def save(self,*args,**kwargs):
    #     if not self.id:
    #         super().save(*args,**kwargs)
    #         grupo = Group.objects.get(name = 'perfilnormal')
    #         if grupo:
    #             self.groups.add(grupo)
    #         super().save(*args,**kwargs)


class UsuarioAdministrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)


class UsuarioGestor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)


class UsuarioNormal(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)



