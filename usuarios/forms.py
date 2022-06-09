import random
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import HiddenInput, TextInput, ValidationError
from django.forms import ModelChoiceField
from django.core.mail import send_mail
from bootstrap_modal_forms.forms import BSModalModelForm
from django.utils.crypto import get_random_string

from ciclo_phva.models import (
    Evidencia,
    Formato,
    EstadoItemEstandar,
    ItemEstandar,
)

from usuarios.models import (
    Usuario,
)

from django.contrib.auth.models import Group



class AccesoUsuarioForm(BSModalModelForm):

    users = forms.ModelChoiceField(queryset = Usuario.objects.filter(es_usuario = True))

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


class UsuarioForm(BSModalModelForm, UserCreationForm):

    es_usuario = forms.BooleanField(initial=True, widget=forms.HiddenInput(), label='')
    password1 = forms.CharField(initial='cintesst', widget=forms.HiddenInput(), label='')
    password2 = forms.CharField(initial='cintesst', widget=forms.HiddenInput(), label='')

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'es_usuario']

class AdminForm(BSModalModelForm, UserCreationForm):

    es_administrador = forms.BooleanField(initial=True, widget=forms.HiddenInput(), label='')
    password1 = forms.CharField(initial='cintesst', widget=forms.HiddenInput(), label='')
    password2 = forms.CharField(initial='cintesst', widget=forms.HiddenInput(), label='')

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'es_administrador']

class CambiarParsswordForm(BSModalModelForm):

    password1 = forms.CharField(initial='cintesst',  widget = forms.PasswordInput(), label='')
    password2 = forms.CharField(initial='cintesst',  widget = forms.PasswordInput(), label='')

    class Meta:
        model = Usuario
        fields = ['password1', 'password2']

    def clean_password2(self):
        """ Validación de Contraseña

        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base dedatos, Retornar la contraseña Válida.

        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2
