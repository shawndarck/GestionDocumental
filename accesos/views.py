from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from ciclo_phva.models import (
    Evidencia,
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

from ciclo_phva.models import ItemEstandar
from accesos.forms import AccesoUsuarioForm
from usuarios.models import Usuario


class PermisosPlanearCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/modal_permisos.html'
    form_class = AccesoUsuarioForm
    success_url = "/accesos_planear/"

    def form_valid(self, form, **kwargs):
        self.object = self.get_object()
        item:(ItemEstandar) = ItemEstandar.objects.get(id=self.object.pk) # Obtener pk de la url con self.object.pk y self.get_object()
        # Acceder al id de la fk con .id
        usu_pk:(int) = self.request.POST.get('users')
        usuario:(Usuario) = Usuario.objects.get(id=usu_pk)
        item.permisos_usuarios.add(usuario)

        return HttpResponseRedirect(self.get_success_url())


class PermisosHacerCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/modal_permisos.html'
    form_class = AccesoUsuarioForm
    success_url = "/accesos_hacer/"

    def form_valid(self, form, **kwargs):
        self.object = self.get_object()
        item:(ItemEstandar) = ItemEstandar.objects.get(id=self.object.pk) # Obtener pk de la url con self.object.pk y self.get_object()
        # Acceder al id de la fk con .id
        usu_pk:(int) = self.request.POST.get('users')
        usuario:(Usuario) = Usuario.objects.get(id=usu_pk)
        item.permisos_usuarios.add(usuario)

        return HttpResponseRedirect(self.get_success_url())


class PermisosVerificarCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/modal_permisos.html'
    form_class = AccesoUsuarioForm
    success_url = "/accesos_verificar/"

    def form_valid(self, form, **kwargs):
        self.object = self.get_object()
        item:(ItemEstandar) = ItemEstandar.objects.get(id=self.object.pk) # Obtener pk de la url con self.object.pk y self.get_object()
        # Acceder al id de la fk con .id
        usu_pk:(int) = self.request.POST.get('users')
        usuario:(Usuario) = Usuario.objects.get(id=usu_pk)
        item.permisos_usuarios.add(usuario)

        return HttpResponseRedirect(self.get_success_url())


class PermisosActuarCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/modal_permisos.html'
    form_class = AccesoUsuarioForm
    success_url = "/accesos_actuar/"

    def form_valid(self, form, **kwargs):
        self.object = self.get_object()
        item:(ItemEstandar) = ItemEstandar.objects.get(id=self.object.pk) # Obtener pk de la url con self.object.pk y self.get_object()
        # Acceder al id de la fk con .id
        usu_pk:(int) = self.request.POST.get('users')
        usuario:(Usuario) = Usuario.objects.get(id=usu_pk)
        item.permisos_usuarios.add(usuario)

        return HttpResponseRedirect(self.get_success_url())


class PermisosReadView(generic.ListView):
    model = Usuario
    template_name = 'usuarios/leer_accesos.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(PermisosReadView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['usuarios'] =  Usuario.objects.filter(itemestandar__in=[pk])
        context['item'] = ItemEstandar.objects.get(id=pk)
        return context



def quitar_acceso(request, pk, id):
    # dictionary for initial data with  
    # field names as keys 
    context ={} 

    # fetch the object related to passed id 
    usu = get_object_or_404(Usuario, id = pk)
    item = get_object_or_404(ItemEstandar, id = id)


    if request.method =="POST": 
        # delete object 
        usu.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/") 

    return reverse_lazy('planear')

class QuitarAcceso(generic.ListView, LoginRequiredMixin):
    item = Usuario
    context_object_name = 'usuario'
    template_name = 'usuarios/eliminar_acceso.html'
    http_method_names = ['post', 'get']

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(QuitarAcceso, self).get_context_data(**kwargs) 
        context['usu'] = Usuario.objects.get(id=self.kwargs.get('pk'))
        return context


    def post(self, request, *args, **kwargs):
        usu = Usuario.objects.get(id=self.kwargs.get('pk'))
        item = ItemEstandar.objects.get(id=self.kwargs.get('id'))
        item.permisos_usuarios.remove(usu)
        return HttpResponseRedirect(reverse_lazy('accesos_planear'))


class GestionPermisosEvidencias(generic.ListView, LoginRequiredMixin):
    item = Usuario
    context_object_name = 'item'
    template_name = 'usuarios/evidencias_usuarios.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(GestionPermisosEvidencias, self).get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.filter(es_usuario = True)
        return context


class AccesosPlanear(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item'
    template_name = 'usuarios/accesos_planear.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(AccesosPlanear, self).get_context_data(**kwargs)
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


class AccesosHacer(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item'
    template_name = 'usuarios/accesos_hacer.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(AccesosHacer, self).get_context_data(**kwargs)
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


class AccesosVerificar(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item'
    template_name = 'usuarios/accesos_verificar.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(AccesosVerificar, self).get_context_data(**kwargs)
        # Contextos individuales (Objeto)
        context['ciclo'] = Ciclo.objects.get(id = 3)
        context['estandar'] = Estandar.objects.get(id = 6)
        context['sub_estandar'] = SubEstandar.objects.get(id = 20)
        # Items de estandar (Lista)
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 20)
        return context


class AccesosActuar(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item'
    template_name = 'usuarios/accesos_actuar.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(AccesosActuar, self).get_context_data(**kwargs)

        # Contextos individuales (Objeto)
        context['ciclo'] = Ciclo.objects.get(id = 4)
        context['estandar'] = Estandar.objects.get(id = 7)
        context['sub_estandar'] = SubEstandar.objects.get(id = 21)
        # Items de estandar (Lista)
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 21)
        return context
