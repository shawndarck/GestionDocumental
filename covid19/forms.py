from django.forms import ValidationError
from bootstrap_modal_forms.forms import BSModalModelForm

from . models import (
    Epidemiologia,
    PruebasCovid,
    RegistroAnual,
    IncapacidadesCovid,
    Incidencia,
    TipoCasoSospechoso,
)


class RegistroAnualForm(BSModalModelForm):

    class Meta:
        model = RegistroAnual
        fields = ['descripcion']


class PruebasCovidForm(BSModalModelForm):

    class Meta:
        model = PruebasCovid
        fields = ['casos_sospechosos', 'positivos', 'negativos', 'sin_prueba']


class EpidemiologiaForm(BSModalModelForm):

    class Meta:
        model = Epidemiologia
        fields = ['casos_sospechosos', 'hospitalizados', 'sintomaticos_recuperados', 'asintomaticos', 'fallecidos']


class IncapacidadesCovidForm(BSModalModelForm):

    class Meta:
        model = IncapacidadesCovid
        fields = ['casos_positivos_con_incapacidad', 'numero_incapacidades', 'numero_dias_perdidos_covid', 'casos_negativos_sin_prueba_con_incapacidad', 'numero_dias_perdidos_sospecha']


class IncidenciaForm(BSModalModelForm):

    class Meta:
        model = Incidencia
        fields = ['numero_casos', 'numero_trabajadores']


class TipoCasoSospechosoForm(BSModalModelForm):

    class Meta:
        model = TipoCasoSospechoso
        fields = ['casos_por_sintomas', 'contacto_directo', 'contacto_indirecto', 'antes_de_ingreso_cinte', 'otros']