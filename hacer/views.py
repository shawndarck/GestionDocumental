from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from ciclo_phva.models import (
    ItemEstandar,
    Evidencia,
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

# Create your views here.

class Hacer(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item_estandar'
    template_name = 'usuarios/hacer.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(Hacer, self).get_context_data(**kwargs)
        lista_items:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=14)
        lista_items2:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=15)
        lista_items3:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=16)
        lista_items4:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=17)
        lista_items5:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=18)
        lista_items6:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=19)
        
        lista_calculo_estandar:(SubEstandar) = SubEstandar.objects.filter(fk_estandar_id=3)
        lista_calculo_estandar2:(SubEstandar) = SubEstandar.objects.filter(fk_estandar_id=4)
        lista_calculo_estandar3:(SubEstandar) = SubEstandar.objects.filter(fk_estandar_id=5)

        lista_estandares:(Estandar) = Estandar.objects.filter(fk_ciclo_id=2)

        #Campos para acceder a la bd (Actualizar)
        sub_estandar:(SubEstandar) = SubEstandar.objects.get(id=14)
        sub_estandar2:(SubEstandar) = SubEstandar.objects.get(id=15)
        sub_estandar3:(SubEstandar) = SubEstandar.objects.get(id=16)
        sub_estandar4:(SubEstandar) = SubEstandar.objects.get(id=17)
        sub_estandar5:(SubEstandar) = SubEstandar.objects.get(id=18)
        sub_estandar6:(SubEstandar) = SubEstandar.objects.get(id=19)
        
        estandar:(Estandar) = Estandar.objects.get(id=3)
        estandar2:(Estandar) = Estandar.objects.get(id=4)
        estandar3:(Estandar) = Estandar.objects.get(id=5)

        ciclos:(Ciclo) = Ciclo.objects.all()
        phva:(Phva) = Phva.objects.get(id=1)
        
        ciclo:(Ciclo) = Ciclo.objects.get(id=2)
        acumulador:(int) = 0
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

        for i in lista_items3:
            acumulador += i.puntaje_obtenido
        sub_estandar3.calificacion_obtenida = acumulador
        if sub_estandar3.calificacion_obtenida != 0:
            coefiente = sub_estandar3.calificacion_maxima / sub_estandar3.calificacion_obtenida
            sub_estandar3.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar3.porcentaje_obtenido = 0
        sub_estandar3.save(update_fields=[ 'calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0

        for i in lista_items4:
            acumulador += i.puntaje_obtenido
        sub_estandar4.calificacion_obtenida = acumulador
        if sub_estandar4.calificacion_obtenida != 0:
            coefiente = sub_estandar4.calificacion_maxima / sub_estandar4.calificacion_obtenida
            sub_estandar4.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar4.porcentaje_obtenido = 0
        sub_estandar4.save(update_fields=[ 'calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0

        for i in lista_items5:
            acumulador += i.puntaje_obtenido
        sub_estandar5.calificacion_obtenida = acumulador
        if sub_estandar5.calificacion_obtenida != 0:
            coefiente = sub_estandar5.calificacion_maxima / sub_estandar5.calificacion_obtenida
            sub_estandar5.porcentaje_obtenido = 100 / coefiente
        else:
            sub_estandar5.porcentaje_obtenido = 0
        sub_estandar5.save(update_fields=[ 'calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0

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

        for i in lista_calculo_estandar3:
            acumulador += i.calificacion_obtenida
        estandar3.calificacion_obtenida = acumulador
        if estandar3.calificacion_obtenida != 0:
            coefiente = estandar3.calificacion_maxima / estandar3.calificacion_obtenida
            estandar3.porcentaje_obtenido = 100 / coefiente
        else:
            estandar3.porcentaje_obtenido = 0
        estandar3.save(update_fields=['calificacion_obtenida', 'porcentaje_obtenido'])
        acumulador = 0

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

        for i in ciclos:
            acumulador += i.calificacion_obtenida
        phva.calificacion_obtenida = acumulador
        phva.save(update_fields=['calificacion_obtenida'])

        # Contextos individuales (Objeto)
        context['ciclo'] = Ciclo.objects.get(id = 2)
        context['estandar'] = Estandar.objects.get(id = 3)
        context['estandar2'] = Estandar.objects.get(id = 4)
        context['estandar3'] = Estandar.objects.get(id = 5)
        context['sub_estandar'] = SubEstandar.objects.get(id = 14)
        context['sub_estandar2'] = SubEstandar.objects.get(id = 15)
        context['sub_estandar3'] = SubEstandar.objects.get(id = 16)
        context['sub_estandar4'] = SubEstandar.objects.get(id = 17)
        context['sub_estandar5'] = SubEstandar.objects.get(id = 18)
        context['sub_estandar6'] = SubEstandar.objects.get(id = 19)
        # Items de estandar (Lista)
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 14)
        context['item_estandar2'] = ItemEstandar.objects.filter(fk_sub_estandar = 15)
        context['item_estandar3'] = ItemEstandar.objects.filter(fk_sub_estandar = 16)
        context['item_estandar4'] = ItemEstandar.objects.filter(fk_sub_estandar = 17)
        context['item_estandar5'] = ItemEstandar.objects.filter(fk_sub_estandar = 18)
        context['item_estandar6'] = ItemEstandar.objects.filter(fk_sub_estandar = 19)
        return context


class HacerUsunormal(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item_estandar'
    template_name = 'usuarios/usunormal_hacer.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(HacerUsunormal, self).get_context_data(**kwargs)
        
        # Contextos individuales (Objeto)
        context['ciclo'] = Ciclo.objects.get(id = 2)
        context['estandar'] = Estandar.objects.get(id = 3)
        context['estandar2'] = Estandar.objects.get(id = 4)
        context['estandar3'] = Estandar.objects.get(id = 5)
        context['sub_estandar'] = SubEstandar.objects.get(id = 14)
        context['sub_estandar2'] = SubEstandar.objects.get(id = 15)
        context['sub_estandar3'] = SubEstandar.objects.get(id = 16)
        context['sub_estandar4'] = SubEstandar.objects.get(id = 17)
        context['sub_estandar5'] = SubEstandar.objects.get(id = 18)
        context['sub_estandar6'] = SubEstandar.objects.get(id = 19)
        # Items de estandar (Lista)
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 14)
        context['item_estandar2'] = ItemEstandar.objects.filter(fk_sub_estandar = 15)
        context['item_estandar3'] = ItemEstandar.objects.filter(fk_sub_estandar = 16)
        context['item_estandar4'] = ItemEstandar.objects.filter(fk_sub_estandar = 17)
        context['item_estandar5'] = ItemEstandar.objects.filter(fk_sub_estandar = 18)
        context['item_estandar6'] = ItemEstandar.objects.filter(fk_sub_estandar = 19)
        return context


class ItemEstadoHacerUpdateView(BSModalUpdateView):
    model = ItemEstandar
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = EstadoItemForm
    success_message = 'Success: Book was updated.'
    success_url = "/hacer/hacer"

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

class EvidenciaHacerDeleteView(BSModalDeleteView):
    model = Evidencia
    template_name = 'usuarios/eliminar_evidencia.html'
    success_message = 'Success: evidencia borrada.'
    success_url = reverse_lazy('hacer')

    def get_success_url(self):
        if self.request.user.es_administrador:
            return reverse_lazy('hacer')
        elif self.request.user.es_gestor:
            return reverse_lazy('hacer_usuario')
