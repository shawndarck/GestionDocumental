from bootstrap_modal_forms.forms import BSModalForm
from django import forms


from ciclo_phva.models import ItemEstandar

from covid19.models import RegistroAnual
from covid19.models import CasosCliente

class GenerarGraficoForm(BSModalForm):

    anual = forms.ModelChoiceField(queryset=RegistroAnual.objects.all())

    class Meta:
        fields = ['anual']


class GenerarGraficoCasoUsuarioForm(BSModalForm):

    cliente = forms.ModelChoiceField(queryset=CasosCliente.objects.all())
    anual = forms.ModelChoiceField(queryset=RegistroAnual.objects.all())

    class Meta:
        fields = ['cliente', 'anual']

