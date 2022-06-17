from django.http import HttpResponseRedirect
from django.shortcuts import render

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
from ciclo_phva.forms import EstadoItemForm

from ciclo_phva.models import (
    Evidencia,
    ItemEstandar,
    SubEstandar,
    Estandar,
    Ciclo,
    Phva,
)


class Actuar(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item_estandar'
    template_name = 'usuarios/actuar.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(Actuar, self).get_context_data(**kwargs)
        # public ItemEstandar lista_items
        lista_items:(ItemEstandar) = ItemEstandar.objects.filter(fk_sub_estandar=21)

        lista_calculo_estandar:(SubEstandar) = SubEstandar.objects.filter(fk_estandar_id=7)

        lista_estandares:(Estandar) = Estandar.objects.filter(fk_ciclo_id=4)

        #Campos para acceder a la bd (Actualizar)
        sub_estandar:(SubEstandar) = SubEstandar.objects.get(id=21)
        
        estandar:(Estandar) = Estandar.objects.get(id=7)

        ciclos:(Ciclo) = Ciclo.objects.all()
        phva:(Phva) = Phva.objects.get(id=1)
        
        ciclo:(Ciclo) = Ciclo.objects.get(id=4)
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
        context['ciclo'] = Ciclo.objects.get(id = 4)
        context['estandar'] = Estandar.objects.get(id = 7)
        context['sub_estandar'] = SubEstandar.objects.get(id = 21)
        # Items de estandar (Lista)
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 21)
        return context


class ActuarUsunormal(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item_estandar'
    template_name = 'usuarios/usunormal_actuar.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(ActuarUsunormal, self).get_context_data(**kwargs)
        # public ItemEstandar lista_items
        
        # Contextos individuales (Objeto)
        context['ciclo'] = Ciclo.objects.get(id = 4)
        context['estandar'] = Estandar.objects.get(id = 7)
        context['sub_estandar'] = SubEstandar.objects.get(id = 21)
        # Items de estandar (Lista)
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 21)
        return context


class ItemEstadoActuarUpdateView(BSModalUpdateView):
    model = ItemEstandar
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = EstadoItemForm
    success_message = 'Success: Book was updated.'
    success_url = "/actuar/actuar"

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


class EvidenciaActuarDeleteView(BSModalDeleteView):
    model = Evidencia
    template_name = 'usuarios/eliminar_evidencia.html'
    success_message = 'Success: evidencia borrada.'
    success_url = "/actuar/actuar"

