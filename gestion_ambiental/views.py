from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from gestion_ambiental.forms import EvidenciaGestionAmbientalForm

from . models import PoliticaGestionAmbiental, EvidenciaGestionAmbiental

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

class GestionAmbientalListView(generic.ListView, LoginRequiredMixin):
    item = PoliticaGestionAmbiental
    context_object_name = 'item_estandar'
    template_name = 'usuarios/gestion_ambiental.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(GestionAmbientalListView, self).get_context_data(**kwargs)
        context['gestion_ambiental'] = PoliticaGestionAmbiental.objects.all()
        return context


class EvidenciaGestionAmbientalCreateView(BSModalCreateView):
    model = EvidenciaGestionAmbiental
    template_name = 'usuarios/crear_evidencia.html'
    form_class = EvidenciaGestionAmbientalForm
    success_message = 'Evidencia creada correctamente'
    success_url = reverse_lazy('gestion_ambiental')

    def form_valid(self, form):
        form.instance.fk_gestion_ambiental_id = self.kwargs.get('pk')
        return super(EvidenciaGestionAmbientalCreateView, self).form_valid(form)


class EvidenciaGestionAmbientalReadView(generic.ListView):
    model = EvidenciaGestionAmbiental
    template_name = 'usuarios/leer_evidencias_ambiental.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(EvidenciaGestionAmbientalReadView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('fk')
        context['evidencias'] = EvidenciaGestionAmbiental.objects.filter(fk_gestion_ambiental = pk)
        return context


class EvidenciaGestionAmbientalDeleteView(BSModalDeleteView):
    model = EvidenciaGestionAmbiental
    template_name = 'usuarios/eliminar_evidencia.html'
    success_message = 'Evidencia borrada.'
    success_url = reverse_lazy('gestion_ambiental')
