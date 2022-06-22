from django.forms import ValidationError
from bootstrap_modal_forms.forms import BSModalModelForm

from . models import (
    Epidemologia,
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


class EpidemologiaForm(BSModalModelForm):

    class Meta:
        model = Epidemologia
        fields = ['casos_sospechosos', 'hospitalizados', 'sintomaticos_recuperados', 'asintomaticos', 'fallecidos']