from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from ciclo_phva.models import (
    Formato,
)

from formatos.forms import FormatoModelForm


class FormatoCreateView(BSModalCreateView):
    template_name = 'usuarios/crear_formato.html'
    model = Formato
    form_class = FormatoModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('formatos_admin')

class FormatosAdmin(generic.ListView, LoginRequiredMixin):
    item = Formato
    template_name = 'usuarios/formatos.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(FormatosAdmin, self).get_context_data(**kwargs)
        context['formatos'] = Formato.objects.all()
        return context



class FormatosUsunormal(generic.ListView, LoginRequiredMixin):
    item = Formato
    template_name = 'usuarios/usuario/formatos.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(FormatosUsunormal, self).get_context_data(**kwargs)
        context['formatos'] = Formato.objects.all()
        return context


class FormatoDeleteView(BSModalDeleteView):
    model = Formato
    template_name = 'usuarios/eliminar_formato.html'
    success_message = 'Success: Formato borrado.'
    success_url = "/formatos_admin/"
