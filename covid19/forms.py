from django.forms import ValidationError
from bootstrap_modal_forms.forms import BSModalModelForm

from . models import (
    PruebasCovid,
    RegistroAnual,
)


class RegistroAnualForm(BSModalModelForm):

    class Meta:
        model = RegistroAnual
        fields = ['descripcion']


class PruebasCovidForm(BSModalModelForm):

    class Meta:
        model = PruebasCovid
        fields = ['casos_sospechosos', 'positivos', 'negativos', 'sin_prueba']