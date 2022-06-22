from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from covid19.forms import (
    RegistroAnualForm,
    PruebasCovidForm,
    EpidemologiaForm,
)

from . models import (
    Epidemologia,
    RegistroAnual,
    PruebasCovid,
)

# Create your views here.
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)


def covid19(request):
    labels = []
    data = []
    positivos:(int) = 0
    negativos:(int) = 0
    sin_prueba:(int) = 0
    fallecidos:(int) = 0

    queryset = PruebasCovid.objects.all()
    for covid19 in queryset:
        positivos += covid19.positivos
        negativos += covid19.negativos
        sin_prueba += covid19.sin_prueba

    data.append(positivos)
    data.append(negativos)
    data.append(sin_prueba)
    data.append(fallecidos)
    labels.append('Positivos')
    labels.append('Negativos')
    labels.append('Sin Prueba')
    labels.append('Fallecidos')

    return render(request, 'usuarios/covid19_central.html', {
        'labels': labels,
        'data': data,
    })


# Gestión de años -----------------------------------------------------------------------------------------------------
class LeerAnualReadView(generic.ListView, LoginRequiredMixin):
    item = RegistroAnual
    context_object_name = 'item_estandar'
    template_name = 'usuarios/leer_anuales.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(LeerAnualReadView, self).get_context_data(**kwargs)
        context['anuales'] = RegistroAnual.objects.all()
        return context


class RegistroAnualCreateView(BSModalCreateView, LoginRequiredMixin):
    model = RegistroAnual
    template_name = 'usuarios/crear_anual.html'
    form_class = RegistroAnualForm
    success_message = 'Registro anual Creado'
    success_url = reverse_lazy('leer_anuales')


class RegistroAnualDeleteView(BSModalDeleteView, LoginRequiredMixin):
    model = RegistroAnual
    template_name = 'usuarios/eliminar_anual.html'
    success_message = 'Success: Registro anual eliminado.'
    success_url = reverse_lazy('leer_anuales')


# Pruebas covid -----------------------------------------------------------------------------------------------------
class PruebasCovidTabla(generic.ListView, LoginRequiredMixin):
    item = PruebasCovid
    context_object_name = 'pruebas_covid'
    template_name = 'usuarios/pruebas_covid.html'

    def get_queryset(self):
        pass
    """
    Esta función tiene dos ciclos que crean registros de pruebas covid según el año registrado
    Maneja un ciclo de creación y eliminacion a partir de validaciones dentro de los bucles
    """
    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(PruebasCovidTabla, self).get_context_data(**kwargs)
        # Ciclo de creación de pruebas covid a partir de un año nuevo
        for anual in RegistroAnual.objects.all():
            if not PruebasCovid.objects.filter(fk_registro_anual_id=anual.id):
                PruebasCovid.objects.create(fk_registro_anual = anual, casos_sospechosos = 0, positivos = 0, negativos = 0, sin_prueba = 0, total = 0)
        context['pruebas_covid'] = PruebasCovid.objects.all()
        return context


class PruebasCovidUpdateView(BSModalUpdateView):
    model = PruebasCovid
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = PruebasCovidForm
    success_message = 'Success: prueba covid actualizada.'
    success_url = reverse_lazy('pruebas_covid')


    def form_valid(self, form):
        prueba = form.save(commit=False)
        prueba.total = prueba.casos_sospechosos + prueba.positivos + prueba.negativos + prueba.sin_prueba
        prueba.save()
        return super().form_valid(form)


class PruebasCovidTabla(generic.ListView, LoginRequiredMixin):
    item = PruebasCovid
    context_object_name = 'pruebas_covid'
    template_name = 'usuarios/pruebas_covid.html'

    def get_queryset(self):
        pass
    """
    Esta función tiene dos ciclos que crean registros de pruebas covid según el año registrado
    Maneja un ciclo de creación y eliminacion a partir de validaciones dentro de los bucles
    """
    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(PruebasCovidTabla, self).get_context_data(**kwargs)
        # Ciclo de creación de pruebas covid a partir de un año nuevo
        for anual in RegistroAnual.objects.all():
            if not PruebasCovid.objects.filter(fk_registro_anual_id=anual.id):
                PruebasCovid.objects.create(fk_registro_anual = anual, casos_sospechosos = 0, positivos = 0, negativos = 0, sin_prueba = 0, total = 0)
        context['pruebas_covid'] = PruebasCovid.objects.all()
        return context


# Epidemología ------------------------------------------------------------------------------------------------

class EpidemologiaTabla(generic.ListView, LoginRequiredMixin):
    item = Epidemologia
    context_object_name = 'epidemologia'
    template_name = 'usuarios/epidemologia.html'

    def get_queryset(self):
        pass
    """
    Esta función tiene dos ciclos que crean registros de pruebas covid según el año registrado
    Maneja un ciclo de creación y eliminacion a partir de validaciones dentro de los bucles
    """
    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(EpidemologiaTabla, self).get_context_data(**kwargs)
        # Ciclo de creación de pruebas covid a partir de un año nuevo
        for anual in RegistroAnual.objects.all():
            if not Epidemologia.objects.filter(fk_registro_anual_id=anual.id):
                Epidemologia.objects.create(fk_registro_anual = anual, casos_sospechosos = 0, hospitalizados = 0, sintomaticos_recuperados = 0, asintomaticos = 0, fallecidos = 0)
        context['epidemologia'] = Epidemologia.objects.all()
        return context


class EpidemologiaUpdateView(BSModalUpdateView):
    model = Epidemologia
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = EpidemologiaForm
    success_message = 'Success: Epidemologia actualizada.'
    success_url = reverse_lazy('epidemologia')