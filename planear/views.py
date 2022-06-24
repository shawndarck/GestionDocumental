from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from ciclo_phva.models import (
    ItemEstandar,
    SubEstandar,
    Estandar,
    Ciclo,
    Phva,
)

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from ciclo_phva.forms import EstadoItemForm
from evidencias.forms import EvidenciaModelForm
from ciclo_phva.models import Evidencia


class Planear(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item_estandar'
    template_name = 'usuarios/planear.html'
    

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(Planear, self).get_context_data(**kwargs)
        lista_items:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=1)
        lista_items2:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=2)
        lista_items3:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=3)
        lista_items4:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=4)
        lista_items5:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=5)
        lista_items6:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=6)
        lista_items7:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=7)
        lista_items8:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=8)
        lista_items9:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=9)
        lista_items10:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=10)
        lista_items11:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=11)
        lista_items12:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=12)
        lista_items13:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=13)
        
        lista_calculo_estandar:(SubEstandar) = SubEstandar.objects.filter(fk_estandar_id=1)
        lista_calculo_estandar2:(SubEstandar) = SubEstandar.objects.filter(fk_estandar_id=2)

        lista_estandares:(Estandar) = Estandar.objects.filter(fk_ciclo_id=1)

        #Campos para acceder a la bd (Actualizar)
        sub_estandar:(SubEstandar) = SubEstandar.objects.get(id=1)
        sub_estandar2:(SubEstandar) = SubEstandar.objects.get(id=2)
        sub_estandar3:(SubEstandar) = SubEstandar.objects.get(id=3)
        sub_estandar4:(SubEstandar) = SubEstandar.objects.get(id=4)
        sub_estandar5:(SubEstandar) = SubEstandar.objects.get(id=5)
        sub_estandar6:(SubEstandar) = SubEstandar.objects.get(id=6)
        sub_estandar7:(SubEstandar) = SubEstandar.objects.get(id=7)
        sub_estandar8:(SubEstandar) = SubEstandar.objects.get(id=8)
        sub_estandar9:(SubEstandar) = SubEstandar.objects.get(id=9)
        sub_estandar10:(SubEstandar) = SubEstandar.objects.get(id=10)
        sub_estandar11:(SubEstandar) = SubEstandar.objects.get(id=11)
        sub_estandar12:(SubEstandar) = SubEstandar.objects.get(id=12)
        sub_estandar13:(SubEstandar) = SubEstandar.objects.get(id=13)
        
        estandar:(Estandar) = Estandar.objects.get(id=1)
        estandar2:(Estandar) = Estandar.objects.get(id=2)
        
        ciclo:(Ciclo) = Ciclo.objects.get(id=1)
        ciclos:(Ciclo) = Ciclo.objects.all()
        phva:(Phva) = Phva.objects.get(id=1)
        acumulador:(float) = 0
        coefiente:(float) = 0
        #Terminar el otro sub estandar (lista y for)
        for i in lista_items:
            acumulador += i.puntaje_obtenido
        sub_estandar.calificacion_obtenida = acumulador
        if sub_estandar.calificacion_obtenida != 0:
            coefiente = sub_estandar.calificacion_maxima / sub_estandar.calificacion_obtenida
            sub_estandar.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar.porcentaje_obtenido = 0
        sub_estandar.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items2:
            acumulador += i.puntaje_obtenido
        sub_estandar2.calificacion_obtenida = acumulador
        if sub_estandar2.calificacion_obtenida != 0:
            coefiente = sub_estandar2.calificacion_maxima / sub_estandar2.calificacion_obtenida
            sub_estandar2.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar2.porcentaje_obtenido = 0
        sub_estandar2.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items3:
            acumulador += i.puntaje_obtenido
        sub_estandar3.calificacion_obtenida = acumulador
        if sub_estandar3.calificacion_obtenida != 0:
            coefiente = sub_estandar3.calificacion_maxima / sub_estandar3.calificacion_obtenida
            sub_estandar3.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar3.porcentaje_obtenido = 0
        sub_estandar3.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items4:
            acumulador += i.puntaje_obtenido
        sub_estandar4.calificacion_obtenida = acumulador
        if sub_estandar4.calificacion_obtenida != 0:
            coefiente = sub_estandar4.calificacion_maxima / sub_estandar4.calificacion_obtenida
            sub_estandar4.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar4.porcentaje_obtenido = 0
        sub_estandar4.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items5:
            acumulador += i.puntaje_obtenido
        sub_estandar5.calificacion_obtenida = acumulador
        if sub_estandar5.calificacion_obtenida != 0:
            coefiente = sub_estandar5.calificacion_maxima / sub_estandar5.calificacion_obtenida
            sub_estandar5.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar5.porcentaje_obtenido = 0
        sub_estandar5.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items6:
            acumulador += i.puntaje_obtenido
        sub_estandar6.calificacion_obtenida = acumulador
        if sub_estandar6.calificacion_obtenida != 0:
            coefiente = sub_estandar6.calificacion_maxima / sub_estandar6.calificacion_obtenida
            sub_estandar6.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar6.porcentaje_obtenido = 0
        sub_estandar6.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items7:
            acumulador += i.puntaje_obtenido
        sub_estandar7.calificacion_obtenida = acumulador
        if sub_estandar7.calificacion_obtenida != 0:
            coefiente = sub_estandar7.calificacion_maxima / sub_estandar7.calificacion_obtenida
            sub_estandar7.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar7.porcentaje_obtenido = 0
        sub_estandar7.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items8:
            acumulador += i.puntaje_obtenido
        sub_estandar8.calificacion_obtenida = acumulador
        if sub_estandar8.calificacion_obtenida != 0:
            coefiente = sub_estandar8.calificacion_maxima / sub_estandar8.calificacion_obtenida
            sub_estandar8.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar8.porcentaje_obtenido = 0
        sub_estandar8.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items9:
            acumulador += i.puntaje_obtenido
        sub_estandar9.calificacion_obtenida = acumulador
        if sub_estandar9.calificacion_obtenida != 0:
            coefiente = sub_estandar9.calificacion_maxima / sub_estandar9.calificacion_obtenida
            sub_estandar9.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar9.porcentaje_obtenido = 0
        sub_estandar9.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items10:
            acumulador += i.puntaje_obtenido
        sub_estandar10.calificacion_obtenida = acumulador
        if sub_estandar10.calificacion_obtenida != 0:
            coefiente = sub_estandar10.calificacion_maxima / sub_estandar10.calificacion_obtenida
            sub_estandar10.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar10.porcentaje_obtenido = 0
        sub_estandar10.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items11:
            acumulador += i.puntaje_obtenido
        sub_estandar11.calificacion_obtenida = acumulador
        if sub_estandar11.calificacion_obtenida != 0:
            coefiente = sub_estandar11.calificacion_maxima / sub_estandar11.calificacion_obtenida
            sub_estandar11.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar11.porcentaje_obtenido = 0
        sub_estandar11.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items12:
            acumulador += i.puntaje_obtenido
        sub_estandar12.calificacion_obtenida = acumulador
        if sub_estandar12.calificacion_obtenida != 0:
            coefiente = sub_estandar12.calificacion_maxima / sub_estandar12.calificacion_obtenida
            sub_estandar12.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar12.porcentaje_obtenido = 0
        sub_estandar12.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_items13:
            acumulador += i.puntaje_obtenido
        sub_estandar13.calificacion_obtenida = acumulador
        if sub_estandar13.calificacion_obtenida != 0:
            coefiente = sub_estandar13.calificacion_maxima / sub_estandar13.calificacion_obtenida
            sub_estandar13.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar13.porcentaje_obtenido = 0
        sub_estandar13.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_calculo_estandar:
            acumulador += i.calificacion_obtenida
        estandar.calificacion_obtenida = acumulador
        if estandar.calificacion_obtenida != 0:
            coefiente = estandar.calificacion_maxima / estandar.calificacion_obtenida
            estandar.porcentaje_obtenido = 100 / coefiente
        else:
            estandar.porcentaje_obtenido = 0
        estandar.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_calculo_estandar2:
            acumulador += i.calificacion_obtenida
        estandar2.calificacion_obtenida = acumulador
        if estandar2.calificacion_obtenida != 0:
            coefiente = estandar2.calificacion_maxima / estandar2.calificacion_obtenida
            estandar2.porcentaje_obtenido = 100 / coefiente
        else:
            estandar2.porcentaje_obtenido = 0
        estandar2.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in lista_estandares:
            acumulador += i.calificacion_obtenida
        ciclo.calificacion_obtenida = acumulador
        if ciclo.calificacion_obtenida != 0:
            coefiente = ciclo.calificacion_maxima / ciclo.calificacion_obtenida
            ciclo.porcentaje_obtenido = 100 / coefiente
        else:
            ciclo.porcentaje_obtenido = 0
        ciclo.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0
        coefiente = 0

        for i in ciclos:
            acumulador += i.calificacion_obtenida
        phva.calificacion_obtenida = acumulador
        phva.save(update_fields=['calificacion_obtenida'])

        # Contextos individuales (Objeto)
        context['ciclo'] = Ciclo.objects.get(id = 1)
        context['estandar'] = Estandar.objects.get(id = 1)
        context['estandar2'] = Estandar.objects.get(id = 2)
        context['sub_estandar'] = SubEstandar.objects.get(id = 1)
        context['sub_estandar2'] = SubEstandar.objects.get(id = 2)
        context['sub_estandar3'] = SubEstandar.objects.get(id = 3)
        context['sub_estandar4'] = SubEstandar.objects.get(id = 4)
        context['sub_estandar5'] = SubEstandar.objects.get(id = 5)
        context['sub_estandar6'] = SubEstandar.objects.get(id = 6)
        context['sub_estandar7'] = SubEstandar.objects.get(id = 7)
        context['sub_estandar8'] = SubEstandar.objects.get(id = 8)
        context['sub_estandar9'] = SubEstandar.objects.get(id = 9)
        context['sub_estandar10'] = SubEstandar.objects.get(id = 10)
        context['sub_estandar11'] = SubEstandar.objects.get(id = 11)
        context['sub_estandar12'] = SubEstandar.objects.get(id = 12)
        context['sub_estandar13'] = SubEstandar.objects.get(id = 13)
        # Items de estandar (Lista)
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 1)
        context['item_estandar2'] = ItemEstandar.objects.filter(fk_sub_estandar = 2)
        context['item_estandar3'] = ItemEstandar.objects.filter(fk_sub_estandar = 3)
        context['item_estandar4'] = ItemEstandar.objects.filter(fk_sub_estandar = 4)
        context['item_estandar5'] = ItemEstandar.objects.filter(fk_sub_estandar = 5)
        context['item_estandar6'] = ItemEstandar.objects.filter(fk_sub_estandar = 6)
        context['item_estandar7'] = ItemEstandar.objects.filter(fk_sub_estandar = 7)
        context['item_estandar8'] = ItemEstandar.objects.filter(fk_sub_estandar = 8)
        context['item_estandar9'] = ItemEstandar.objects.filter(fk_sub_estandar = 9)
        context['item_estandar10'] = ItemEstandar.objects.filter(fk_sub_estandar = 10)
        context['item_estandar11'] = ItemEstandar.objects.filter(fk_sub_estandar = 11)
        context['item_estandar12'] = ItemEstandar.objects.filter(fk_sub_estandar = 12)
        context['item_estandar13'] = ItemEstandar.objects.filter(fk_sub_estandar = 13)
        return context


class PlanearUsunormal(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item_estandar'
    template_name = 'usuarios/usunormal_planear.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(PlanearUsunormal, self).get_context_data(**kwargs)
        # Contextos individuales (Objeto)
        context['ciclo'] = Ciclo.objects.get(id = 1)
        context['estandar'] = Estandar.objects.get(id = 1)
        context['estandar2'] = Estandar.objects.get(id = 2)
        context['sub_estandar'] = SubEstandar.objects.get(id = 1)
        context['sub_estandar2'] = SubEstandar.objects.get(id = 2)
        context['sub_estandar3'] = SubEstandar.objects.get(id = 3)
        context['sub_estandar4'] = SubEstandar.objects.get(id = 4)
        context['sub_estandar5'] = SubEstandar.objects.get(id = 5)
        context['sub_estandar6'] = SubEstandar.objects.get(id = 6)
        context['sub_estandar7'] = SubEstandar.objects.get(id = 7)
        context['sub_estandar8'] = SubEstandar.objects.get(id = 8)
        context['sub_estandar9'] = SubEstandar.objects.get(id = 9)
        context['sub_estandar10'] = SubEstandar.objects.get(id = 10)
        context['sub_estandar11'] = SubEstandar.objects.get(id = 11)
        context['sub_estandar12'] = SubEstandar.objects.get(id = 12)
        context['sub_estandar13'] = SubEstandar.objects.get(id = 13)
        # Items de estandar (Lista)
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 1)
        context['item_estandar2'] = ItemEstandar.objects.filter(fk_sub_estandar = 2)
        context['item_estandar3'] = ItemEstandar.objects.filter(fk_sub_estandar = 3)
        context['item_estandar4'] = ItemEstandar.objects.filter(fk_sub_estandar = 4)
        context['item_estandar5'] = ItemEstandar.objects.filter(fk_sub_estandar = 5)
        context['item_estandar6'] = ItemEstandar.objects.filter(fk_sub_estandar = 6)
        context['item_estandar7'] = ItemEstandar.objects.filter(fk_sub_estandar = 7)
        context['item_estandar8'] = ItemEstandar.objects.filter(fk_sub_estandar = 8)
        context['item_estandar9'] = ItemEstandar.objects.filter(fk_sub_estandar = 9)
        context['item_estandar10'] = ItemEstandar.objects.filter(fk_sub_estandar = 10)
        context['item_estandar11'] = ItemEstandar.objects.filter(fk_sub_estandar = 11)
        context['item_estandar12'] = ItemEstandar.objects.filter(fk_sub_estandar = 12)
        context['item_estandar13'] = ItemEstandar.objects.filter(fk_sub_estandar = 13)
        return context


class ItemEstadoUpdateView(BSModalUpdateView):
    model = ItemEstandar
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = EstadoItemForm
    success_message = 'Success: Book was updated.'
    success_url = "/planear/planear/"

    def form_valid(self, form, **kwargs):
        self.object = self.get_object()
        item = ItemEstandar.objects.get(id=self.object.pk) # Obtener pk de la url con self.object.pk y self.get_object()
        puntaje_maximo = item.puntaje_maximo
        # Acceder al id de la fk con .id
        estado = item.fk_estado.id
        if form.instance.fk_estado.id == 1:
            item.puntaje_obtenido = puntaje_maximo
            item.save(update_fields=['puntaje_obtenido'])
        elif form.instance.fk_estado.id == 2:
            item.puntaje_obtenido = 0
            item.save(update_fields=['puntaje_obtenido'])
        elif form.instance.fk_estado.id == 3:
            item.puntaje_obtenido = puntaje_maximo
            item.save(update_fields=['puntaje_obtenido'])
        item.fk_estado = form.instance.fk_estado
        item.save(update_fields=['fk_estado_id'])
        return HttpResponseRedirect(self.get_success_url())


class EvidenciaPlanearCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/crear_evidencia.html'
    form_class = EvidenciaModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('planear')

    def form_valid(self, form):
        form.instance.fk_item_estandar_id = self.kwargs.get('pk')
        return super(EvidenciaPlanearCreateView, self).form_valid(form)


class EvidenciaPlanearDeleteView(BSModalDeleteView):
    model = Evidencia
    template_name = 'usuarios/eliminar_evidencia.html'
    success_message = 'Success: evidencia borrada.'
    success_url = reverse_lazy('planear')



def calificar_planear(request):
    item_estandar = request.GET.get('cumple', None)
    response = {
        'respuesta': ItemEstandar.objects.filter(puntaje=item_estandar).exists()
    }
    return JsonResponse(response)
