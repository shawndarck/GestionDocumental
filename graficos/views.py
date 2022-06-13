from django.shortcuts import render
from ciclo_phva.models import Ciclo

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
