from django.shortcuts import render
from bootstrap_modal_forms.generic import BSModalCreateView

from django.views import generic
from django.urls import reverse_lazy
from ciclo_phva.models import (
    ItemEstandar,
    Evidencia
)
from . forms import EvidenciaModelForm

# Create your views here.
class EvidenciaPlanearCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/crear_evidencia.html'
    form_class = EvidenciaModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('planear')

    def form_valid(self, form):
        form.instance.fk_item_estandar_id = self.kwargs.get('pk')
        return super(EvidenciaPlanearCreateView, self).form_valid(form)

class EvidenciaHacerCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/crear_evidencia.html'
    form_class = EvidenciaModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('hacer')

    def form_valid(self, form):
        form.instance.fk_item_estandar_id = self.kwargs.get('pk')
        return super(EvidenciaHacerCreateView, self).form_valid(form)

class EvidenciaVerificarCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/crear_evidencia.html'
    form_class = EvidenciaModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('verificar')

    def form_valid(self, form):
        form.instance.fk_item_estandar_id = self.kwargs.get('pk')
        return super(EvidenciaVerificarCreateView, self).form_valid(form)

class EvidenciaActuarCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/crear_evidencia.html'
    form_class = EvidenciaModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('actuar')

    def form_valid(self, form):
        form.instance.fk_item_estandar_id = self.kwargs.get('pk')
        return super(EvidenciaActuarCreateView, self).form_valid(form)

class EvidenciaUsuarioReadView(generic.ListView):
    model = Evidencia
    template_name = 'usuarios/leer_evidencias.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(EvidenciaUsuarioReadView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('fk')
        items = ItemEstandar.objects.filter(permisos_usuarios__in=[self.request.user.id])
        item:(ItemEstandar) = ItemEstandar
        for i in items:
            if i.id == pk:
                item = i
                context['evidencias'] = Evidencia.objects.filter(fk_item_estandar = item.id)
                break
        return context

class EvidenciaReadView(generic.ListView):
    model = Evidencia
    template_name = 'usuarios/leer_evidencias.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(EvidenciaReadView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('fk')
        context['evidencias'] = Evidencia.objects.filter(fk_item_estandar = pk)
        return context
