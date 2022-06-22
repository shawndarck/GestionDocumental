from django.forms import ValidationError
from bootstrap_modal_forms.forms import BSModalModelForm

from . models import RegistroAnual


class RegistroAnualForm(BSModalModelForm):

    class Meta:
        model = RegistroAnual
        fields = ['descripcion']
