from django.shortcuts import render
from ciclo_phva.models import Ciclo
from covid19.models import PruebasCovid

# Create your views here.
def bar_chart_phva(request):
    labels = []
    data = []

    queryset = Ciclo.objects.order_by('-id')[:4]
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
