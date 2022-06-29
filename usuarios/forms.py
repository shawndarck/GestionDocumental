import random
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import HiddenInput, TextInput, ValidationError
from django.forms import ModelChoiceField
from django.core.mail import send_mail
from django.core.validators import RegexValidator
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


class UsuarioForm(BSModalModelForm):
    username = forms.CharField()
    password = forms.CharField(initial='cintesettempo', widget=forms.HiddenInput(), label='')

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name']


class AdminForm(BSModalModelForm):

    username = forms.CharField()
    password = forms.CharField(initial='cintesettempo', widget=forms.HiddenInput(), label='')

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name']


class CambiarNombreForm(BSModalModelForm):

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name']



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


class LoginForm(forms.Form):
    email = forms.CharField(label='Correo Electrónico')

    class Meta:
        model = Usuario
        fields = ['email']