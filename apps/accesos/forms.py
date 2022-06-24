from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms


from ciclo_phva.models import ItemEstandar

from usuarios.models import Usuario

class AccesoUsuarioForm(BSModalModelForm):

    users = forms.ModelChoiceField(queryset = Usuario.objects.filter(es_usuario = True))

    class Meta:
        model = ItemEstandar
        fields = ['users']

    def clean_users(self, **kwards):
        data = self.cleaned_data
        users = data['users']
        return users