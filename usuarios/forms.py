
from django.forms import TextInput, ValidationError
from dataclasses import field, fields
import django


from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django import forms

from ciclo_phva.models import (
    Evidencia,
    Formato,
    EstadoItemEstandar,
    ItemEstandar,
)

from usuarios.models import (
    Usuario,
)

from bootstrap_modal_forms.forms import BSModalModelForm
from django.forms import ModelChoiceField




class AccesoUsuarioForm(BSModalModelForm):

    usuarios = []
    for user in Usuario.objects.filter(es_usuario = True):
        usuarios.append((user.id, user.username))

    users = forms.ChoiceField(choices = usuarios)
    class Meta:
        model = ItemEstandar
        fields = ['users']

    def clean_users(self, **kwards):
        data = self.cleaned_data
        users = data['users']
        return users


class EstadoItemForm(BSModalModelForm):

    class Meta:
        model = ItemEstandar
        fields = ['fk_estado']

    def clean_fk_estado(self, **kwards):
        data = self.cleaned_data
        fk_estado = data['fk_estado']
        return fk_estado

class EvidenciaModelForm(BSModalModelForm):

    class Meta:
        model = Evidencia
        fields = ['nombre_evidencia', 'formato']


    def clean_formato(self, **kwargs):
        CONTENT_TYPES = ['pdf','png']
        # 2.5MB - 2621440
        # 5MB - 5242880
        # 10MB - 10485760
        # 20MB - 20971520
        # 50MB - 5242880
        # 100MB 104857600
        # 250MB - 214958080
        # 500MB - 429916160
        MAX_UPLOAD_SIZE = "2621440"
        data = self.cleaned_data
        formato = data['formato']
        content_type = formato.content_type.split('/')[1]
        if content_type in CONTENT_TYPES:
            if formato.size > int(MAX_UPLOAD_SIZE):
                raise ValidationError('El archivo supera los dos 2,5 MB Intenta nuevamente')
        else:
            raise ValidationError('Formato de archivo no válido')
        return formato


class FormatoModelForm(BSModalModelForm):

    class Meta:
        model = Formato
        fields = ['descripcion', 'formato_nombre']


    def clean_formato(self, **kwargs):
        CONTENT_TYPES = ['png', 'pdf', 'xlsx', 'xls', 'docx', 'doc']
        # 2.5MB - 2621440
        # 5MB - 5242880
        # 10MB - 10485760
        # 20MB - 20971520
        # 50MB - 5242880
        # 100MB 104857600
        # 250MB - 214958080
        # 500MB - 429916160
        MAX_UPLOAD_SIZE = "2621440"
        data = self.cleaned_data
        formato = data['formato']
        content_type = formato.content_type.split('/')[1]
        if content_type in CONTENT_TYPES:
            if formato.size > int(MAX_UPLOAD_SIZE):
                raise ValidationError('El archivo supera los dos 2,5 MB Intenta nuevamente')
        else:
            raise ValidationError('Formato de archivo no válido')
        return formato


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']