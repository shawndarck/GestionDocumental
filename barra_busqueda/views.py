from django.shortcuts import render
from django.db.models import  Q# Q es el constructor que permite hacer consultas más avanzadas
from ciclo_phva.models import ItemEstandar


def barra_busqueda(request):
    
    termino_busqueda = request.GET.get('termino') # Obtiene el dato de la barra de busqueda
    # Valida si hay terminos no vacios en el post
    if termino_busqueda: # __icontains permite buscar un termino en una cadena sin importar mayúsculas y minsculas
        respuestas_post = ItemEstandar.objects.filter(Q(descripcion__icontains=termino_busqueda))
    else:    
        respuestas_post = ItemEstandar.objects.all().order_by("-id")

    return render(request, 'usuarios/resultados_busqueda.html', {'respuestas_post': respuestas_post})
