from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import (
    Epidemiologia,
    RegistroAnual,
    PruebasCovid,
    IncapacidadesCovid,
    Incidencia,
    TipoCasoSospechoso,
    CasosCliente,
    CasosAnuales,
)

from covid19.forms import (
    RegistroAnualForm,
    PruebasCovidForm,
    EpidemiologiaForm,
    IncapacidadesCovidForm,
    IncidenciaForm,
    TipoCasoSospechosoForm,
    CasosClienteCreateForm,
    CasosClienteUpdateForm,
    CasosClienteNombreUpdateForm,
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


# Epidemiología ------------------------------------------------------------------------------------------------

class EpidemiologiaTabla(generic.ListView, LoginRequiredMixin):
    item = Epidemiologia
    context_object_name = 'epidemiologia'
    template_name = 'usuarios/epidemiologia.html'

    def get_queryset(self):
        pass
    """
    Esta función tiene dos ciclos que crean registros de pruebas covid según el año registrado
    Maneja un ciclo de creación y eliminacion a partir de validaciones dentro de los bucles
    """
    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(EpidemiologiaTabla, self).get_context_data(**kwargs)
        # Ciclo de creación de pruebas covid a partir de un año nuevo
        for anual in RegistroAnual.objects.all():
            if not Epidemiologia.objects.filter(fk_registro_anual_id=anual.id):
                Epidemiologia.objects.create(fk_registro_anual = anual, casos_sospechosos = 0, hospitalizados = 0, sintomaticos_recuperados = 0, asintomaticos = 0, fallecidos = 0)
        context['epidemiologia'] = Epidemiologia.objects.all()
        return context


class EpidemiologiaUpdateView(BSModalUpdateView):
    model = Epidemiologia
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = EpidemiologiaForm
    success_message = 'Success: Epidemologia actualizada.'
    success_url = reverse_lazy('epidemologia')


# Incapacidades covid ------------------------------------------------------------------------------------------------
class IncapacidadesCovidTabla(generic.ListView, LoginRequiredMixin):
    item = IncapacidadesCovid
    context_object_name = 'incapacidades_covid'
    template_name = 'usuarios/incapacidades_covid.html'

    def get_queryset(self):
        pass
    """
    Esta función tiene dos ciclos que crean registros de pruebas covid según el año registrado
    Maneja un ciclo de creación y eliminacion a partir de validaciones dentro de los bucles
    """
    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(IncapacidadesCovidTabla, self).get_context_data(**kwargs)
        # Ciclo de creación de pruebas covid a partir de un año nuevo
        for anual in RegistroAnual.objects.all():
            if not IncapacidadesCovid.objects.filter(fk_registro_anual_id=anual.id):
                IncapacidadesCovid.objects.create(fk_registro_anual = anual, casos_positivos_con_incapacidad = 0, numero_incapacidades = 0, numero_dias_perdidos_covid = 0, casos_negativos_sin_prueba_con_incapacidad = 0, numero_dias_perdidos_sospecha = 0)
        context['incapacidades_covid'] = IncapacidadesCovid.objects.all()
        return context


class IncapacidadesCovidUpdateView(BSModalUpdateView):
    model = IncapacidadesCovid
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = IncapacidadesCovidForm
    success_message = 'Success: Incapacidad covid actualizada.'
    success_url = reverse_lazy('incapacidades')


# Incidencias ------------------------------------------------------------------------------------------------
class IncidenciasTabla(generic.ListView, LoginRequiredMixin):
    item = Incidencia
    context_object_name = 'incidencias'
    template_name = 'usuarios/incidencias.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(IncidenciasTabla, self).get_context_data(**kwargs)
        # Ciclo de creación de pruebas covid a partir de un año nuevo
        for anual in RegistroAnual.objects.all():
            if not Incidencia.objects.filter(fk_registro_anual_id=anual.id):
                Incidencia.objects.create(fk_registro_anual = anual, numero_casos = 0, numero_trabajadores = 0, porcentaje_incidencia = 0)
        context['incidencias'] = Incidencia.objects.all()
        return context


class IncidenciasUpdateView(BSModalUpdateView):
    model = Incidencia
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = IncidenciaForm
    success_message = 'Success: Incidencia actualizada.'
    success_url = reverse_lazy('incidencias')


# Tipo de caso sospechoso ------------------------------------------------------------------------------------------------
class TipoCasoSospechosoTabla(generic.ListView, LoginRequiredMixin):
    item = TipoCasoSospechoso
    context_object_name = 'tipo_caso_sospechoso'
    template_name = 'usuarios/tipo_caso_sospechoso.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(TipoCasoSospechosoTabla, self).get_context_data(**kwargs)
        # Ciclo de creación de pruebas covid a partir de un año nuevo
        for anual in RegistroAnual.objects.all():
            if not TipoCasoSospechoso.objects.filter(fk_registro_anual_id=anual.id):
                TipoCasoSospechoso.objects.create(fk_registro_anual = anual, casos_por_sintomas = 0, contacto_directo = 0, contacto_indirecto = 0, antes_de_ingreso_cinte = 0, otros = 0)
        context['tipo_caso_sospechosos'] = TipoCasoSospechoso.objects.all()
        return context


class TipoCasoSospechosoUpdateView(BSModalUpdateView):
    model = TipoCasoSospechoso
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = TipoCasoSospechosoForm
    success_message = 'Success: Tipo caso sospechoso actualizado.'
    success_url = reverse_lazy('tipo_caso_sospechoso')


# Casos por cliente ------------------------------------------------------------------------------------------------
class CasosClienteCreateView(BSModalCreateView, LoginRequiredMixin):
    model = CasosCliente
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = CasosClienteCreateForm
    success_message = 'Cliente creado correctamente.'
    success_url = reverse_lazy('casos_cliente')


class CasosClienteTabla(generic.ListView, LoginRequiredMixin):
    item = CasosCliente
    context_object_name = 'casos_cliente'
    template_name = 'usuarios/casos_cliente.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(CasosClienteTabla, self).get_context_data(**kwargs)
        # Ciclo de creación de pruebas covid a partir de un año nuevo
        for casos_cliente in CasosCliente.objects.all():
            for anual in RegistroAnual.objects.all():
                if not CasosAnuales.objects.filter(fk_anual_id=anual.id, fk_casos_cliente_id=casos_cliente.id):
                    casos_cliente.registros_anuales.add(anual)

        acumulador:(int) = 0
        for casos in CasosCliente.objects.all():
            caso_cliente:(CasosCliente) = CasosCliente.objects.get(id=casos.id)
            for anual in CasosAnuales.objects.filter(fk_casos_cliente_id=casos.id):
                if anual.numero_casos:
                    acumulador += anual.numero_casos
            caso_cliente.total_casos = acumulador
            caso_cliente.save()
            acumulador = 0
        context['casos_cliente'] = CasosCliente.objects.all()
        return context


class CasosClienteUpdateView(BSModalUpdateView):
    model = CasosAnuales
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = CasosClienteUpdateForm
    success_message = 'Casos de cliente actualizado.'
    success_url = reverse_lazy('casos_cliente')

    def form_valid(self, form):
        casos = form.save(commit=False)
        acumulador:(int) = 0
        caso_cliente:(CasosCliente) = CasosCliente.objects.get(id=casos.fk_casos_cliente_id)
        for anual in CasosAnuales.objects.filter(fk_casos_cliente_id=casos.fk_casos_cliente):
            if casos.fk_anual_id != anual.fk_anual_id:
                if anual.numero_casos:
                    acumulador += anual.numero_casos
        caso_cliente.total_casos = acumulador + casos.numero_casos
        caso_cliente.save()
        return super().form_valid(form)


class ClienteAnualesReadView(generic.ListView):
    model = CasosCliente
    template_name = 'usuarios/leer_anuales_cliente.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(ClienteAnualesReadView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['anuales'] =  CasosAnuales.objects.filter(fk_casos_cliente_id=pk)
        context['item'] = CasosCliente.objects.get(id=pk)
        return context


class CasoClienteDeleteView(BSModalDeleteView):
    model = CasosCliente
    template_name = 'usuarios/eliminar_caso_cliente.html'
    success_message = 'Cliente eliminado.'
    success_url = reverse_lazy('casos_cliente')


class CasoClienteNombreUpdateView(BSModalUpdateView):
    model = CasosCliente
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = CasosClienteNombreUpdateForm
    success_message = 'Nombre de cliente actualizado.'
    success_url = reverse_lazy('casos_cliente')