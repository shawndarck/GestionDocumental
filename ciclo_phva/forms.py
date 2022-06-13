from bootstrap_modal_forms.forms import BSModalModelForm
from ciclo_phva.models import ItemEstandar

class EstadoItemForm(BSModalModelForm):

    class Meta:
        model = ItemEstandar
        fields = ['fk_estado']

    def clean_fk_estado(self, **kwards):
        data = self.cleaned_data
        fk_estado = data['fk_estado']
        return fk_estado