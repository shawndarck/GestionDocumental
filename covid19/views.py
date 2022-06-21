from django.shortcuts import render

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from ciclo_phva.models import RegistroAnual

# Create your views here.
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)


class Covid19(generic.ListView, LoginRequiredMixin):
    item = RegistroAnual
    context_object_name = 'registro_anual'
    template_name = 'usuarios/covid19_central.html'

    def get_queryset(self):
        pass