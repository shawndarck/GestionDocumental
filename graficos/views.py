from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from ciclo_phva.models import Ciclo
from covid19.models import (
    Epidemiologia,
    RegistroAnual,
    PruebasCovid,
    IncapacidadesCovid,
    Incidencia,
    TipoCasoSospechoso,
    CasosCliente,
    CasosAnuales,
)

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView,
)

from graficos.forms import (
    GenerarGraficoForm,
    GenerarGraficoCasoUsuarioForm,
)


class PruebasCovidFilterView(BSModalFormView):
    template_name = 'usuarios/grafico_filtro.html'
    form_class = GenerarGraficoForm

    def form_valid(self, form):
        self.filter = '?anual=' + str(form.cleaned_data['anual'].pk)
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('grafico_pruebas_covid') + self.filter


class EpidemiologiaFilterView(BSModalFormView):
    template_name = 'usuarios/grafico_filtro.html'
    form_class = GenerarGraficoForm

    def form_valid(self, form):
        self.filter = '?anual=' + str(form.cleaned_data['anual'].pk)
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('grafico_epidemiologia') + self.filter


class IncapacidadesCovidFilterView(BSModalFormView):
    template_name = 'usuarios/grafico_filtro.html'
    form_class = GenerarGraficoForm

    def form_valid(self, form):
        self.filter = '?anual=' + str(form.cleaned_data['anual'].pk)
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('grafico_incapacidades') + self.filter


class IncidenciaFilterView(BSModalFormView):
    template_name = 'usuarios/grafico_filtro.html'
    form_class = GenerarGraficoForm

    def form_valid(self, form):
        self.filter = '?anual=' + str(form.cleaned_data['anual'].pk)
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('grafico_incidencias') + self.filter


class TipoCasoSospechosoFilterView(BSModalFormView):
    template_name = 'usuarios/grafico_filtro.html'
    form_class = GenerarGraficoForm

    def form_valid(self, form):
        self.filter = '?anual=' + str(form.cleaned_data['anual'].pk)
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('grafico_tipo_caso_sospechosos') + self.filter


class CasosClienteFilterView(BSModalFormView):
    template_name = 'usuarios/grafico_filtro.html'
    form_class = GenerarGraficoCasoUsuarioForm

    def form_valid(self, form):
        self.filter = '?anual=' + str(form.cleaned_data['anual'].pk) + '&cliente=' + str(form.cleaned_data['cliente'].pk)
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('grafico_casos_cliente') + self.filter


def bar_chart_pruebas_covid(request):
    labels = []
    data = []
    prueba_covid = PruebasCovid.objects.get(fk_registro_anual_id=int(request.GET.get('anual')))

    data.append(prueba_covid.casos_sospechosos)
    data.append(prueba_covid.positivos)
    data.append(prueba_covid.negativos)
    data.append(prueba_covid.sin_prueba)
    data.append(prueba_covid.total)
    labels.append('Casos sospechosos')
    labels.append('Positivos')
    labels.append('Negativos')
    labels.append('Sin prueba')
    labels.append('Totales')

    colors = ['#0F4C5C', '#ff7d00', '#41b751', '#ffc332', '#ffc332']

    return render(request, 'usuarios/grafico_covid19.html', {
        'labels': labels,
        'data': data,
        'colors': colors,
    })


def bar_chart_epidemiologia(request):
    labels = []
    data = []
    epidemiologia = Epidemiologia.objects.get(fk_registro_anual_id=int(request.GET.get('anual')))

    data.append(epidemiologia.casos_sospechosos)
    data.append(epidemiologia.hospitalizados)
    data.append(epidemiologia.sintomaticos_recuperados)
    data.append(epidemiologia.asintomaticos)
    data.append(epidemiologia.fallecidos)

    labels.append('Casos sospechosos')
    labels.append('Hospitalizados')
    labels.append('Sintomaticos recuperados')
    labels.append('Asintomaticos')
    labels.append('Fallecidos')

    colors = ['#0F4C5C', '#ff7d00', '#41b751', '#ffc332', '#ffc332']

    return render(request, 'usuarios/grafico_covid19.html', {
        'labels': labels,
        'data': data,
        'colors': colors,
    })


def bar_chart_incapacidades_covid(request):
    labels = []
    data = []
    incapacidades_covid = IncapacidadesCovid.objects.get(fk_registro_anual_id=int(request.GET.get('anual')))

    data.append(incapacidades_covid.casos_positivos_con_incapacidad)
    data.append(incapacidades_covid.numero_incapacidades)
    data.append(incapacidades_covid.numero_dias_perdidos_covid)
    data.append(incapacidades_covid.casos_negativos_sin_prueba_con_incapacidad)
    data.append(incapacidades_covid.numero_dias_perdidos_sospecha)

    labels.append('Casos positivos con incapacidad')
    labels.append('Número de incapacidades')
    labels.append('Número de dias perdidos')
    labels.append('Casos negativos sin prueba con incapacidad')
    labels.append('Numero de dias perdidos')

    colors = ['#0F4C5C', '#ff7d00', '#41b751', '#ffc332', '#ffc332']

    return render(request, 'usuarios/grafico_covid19.html', {
        'labels': labels,
        'data': data,
        'colors': colors,
    })


def bar_chart_incidencia(request):
    labels = []
    data = []
    incidencia = Incidencia.objects.get(fk_registro_anual_id=int(request.GET.get('anual')))

    data.append(incidencia.numero_casos)
    data.append(incidencia.numero_trabajadores)
    data.append(incidencia.porcentaje_incidencia)

    labels.append('Número de casos')
    labels.append('Número de trabajadores')
    labels.append('Porcentaje de incidencia')

    colors = ['#0F4C5C', '#ff7d00', '#41b751']

    return render(request, 'usuarios/grafico_covid19.html', {
        'labels': labels,
        'data': data,
        'colors': colors,
    })


def bar_chart_tipo_caso_sospechoso(request):
    labels = []
    data = []
    pk = int(request.GET.get('anual'))
    tipo_caso_sospechoso = TipoCasoSospechoso.objects.get(fk_registro_anual_id=int(request.GET.get('anual')))

    data.append(tipo_caso_sospechoso.casos_por_sintomas)
    data.append(tipo_caso_sospechoso.contacto_directo)
    data.append(tipo_caso_sospechoso.contacto_indirecto)
    data.append(tipo_caso_sospechoso.antes_de_ingreso_cinte)
    data.append(tipo_caso_sospechoso.otros)

    labels.append('Casos por sintomas')
    labels.append('Contacto directo')
    labels.append('Contacto indirecto')
    labels.append('Antes de ingreso cinte')
    labels.append('Otros')

    colors = ['#0F4C5C', '#ff7d00', '#41b751', '#ffc332', '#ffc332']

    return render(request, 'usuarios/grafico_covid19.html', {
        'labels': labels,
        'data': data,
        'colors': colors,
    })


def bar_chart_casos_clientes(request):
    labels = []
    data = []
    colors = []
    cliente_casos_anuales = CasosAnuales.objects.get(fk_casos_cliente_id=int(request.GET.get('cliente')), fk_anual_id=int(request.GET.get('anual')))

    if not cliente_casos_anuales.numero_casos:
        data.append(0)
    else:
        data.append(cliente_casos_anuales.numero_casos)

    labels.append('Casos')

    colors = ['#ff7d00']

    return render(request, 'usuarios/grafico_covid19.html', {
        'labels': labels,
        'data': data,
        'colors': colors,
    })


def bar_chart_phva(request):
    labels = []
    data = []

    queryset = Ciclo.objects.all().order_by('id')
    for ciclo in queryset:
        labels.append(ciclo.descripcion)
        data.append(ciclo.calificacion_obtenida)

    return render(request, 'usuarios/grafico.html', {
        'labels': labels,
        'data': data,
    })


def bar_chart_covid19(request):
    labels = []
    data = []
    positivos:(int) = 0
    negativos:(int) = 0
    sin_prueba:(int) = 0

    queryset = PruebasCovid.objects.all()
    for covid19 in queryset:
        positivos += covid19.positivos
        negativos += covid19.negativos
        sin_prueba += covid19.sin_prueba

    data.append(positivos, negativos, sin_prueba, 0)
    labels.append('Positivos', 'Negativos', 'Sin Prueba', 'Fallecidos')

    return render(request, 'usuarios/grafico.html', {
        'labels': labels,
        'data': data,
    })
