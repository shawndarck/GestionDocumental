from ast import For
from decimal import Subnormal
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as dj_login
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from ciclo_phva.models import (
    ItemEstandar,
    Evidencia,
    Formato,
    SubEstandar,
    Estandar,
    Ciclo
)
from .forms import UserRegisterForm
from bootstrap_modal_forms.generic import BSModalCreateView
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
    EvidenciaModelForm,
    FormatoModelForm,
    EstadoItemForm
)

CONTENT_TYPES = ['pdf','png']
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = "2621440"

def index(request):
    documents = Evidencia.objects.all()
    return render(request, "usuarios/index.html", context = {"files": documents})


class EvidenciaCreateView(BSModalCreateView):
    model = ItemEstandar
    template_name = 'usuarios/crear_evidencia.html'
    form_class = EvidenciaModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('planear')

    def form_valid(self, form):
        form.instance.fk_item_estandar_id = self.kwargs.get('pk')
        return super(EvidenciaCreateView, self).form_valid(form)


class EvidenciaReadView(generic.ListView):
    model = Evidencia
    template_name = 'usuarios/leer_evidencias.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(EvidenciaReadView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('fk')
        context['evidencias'] = Evidencia.objects.filter(fk_item_estandar = pk)
        return context


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
        acumulador:(int) = 0 
        #Terminar el otro sub estandar (lista y for)
        for i in lista_items:
            acumulador += i.puntaje_obtenido
        sub_estandar.calificacion_obtenida = acumulador
        sub_estandar.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items2:
            acumulador += i.puntaje_obtenido
        sub_estandar2.calificacion_obtenida = acumulador
        sub_estandar2.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items3:
            acumulador += i.puntaje_obtenido
        sub_estandar3.calificacion_obtenida = acumulador
        sub_estandar3.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items4:
            acumulador += i.puntaje_obtenido
        sub_estandar4.calificacion_obtenida = acumulador
        sub_estandar4.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items5:
            acumulador += i.puntaje_obtenido
        sub_estandar5.calificacion_obtenida = acumulador
        sub_estandar5.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items6:
            acumulador += i.puntaje_obtenido
        sub_estandar6.calificacion_obtenida = acumulador
        sub_estandar6.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items7:
            acumulador += i.puntaje_obtenido
        sub_estandar7.calificacion_obtenida = acumulador
        sub_estandar7.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items8:
            acumulador += i.puntaje_obtenido
        sub_estandar8.calificacion_obtenida = acumulador
        sub_estandar8.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items9:
            acumulador += i.puntaje_obtenido
        sub_estandar9.calificacion_obtenida = acumulador
        sub_estandar9.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items10:
            acumulador += i.puntaje_obtenido
        sub_estandar10.calificacion_obtenida = acumulador
        sub_estandar10.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items11:
            acumulador += i.puntaje_obtenido
        sub_estandar11.calificacion_obtenida = acumulador
        sub_estandar11.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items12:
            acumulador += i.puntaje_obtenido
        sub_estandar12.calificacion_obtenida = acumulador
        sub_estandar12.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items13:
            acumulador += i.puntaje_obtenido
        sub_estandar13.calificacion_obtenida = acumulador
        sub_estandar13.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_calculo_estandar:
            acumulador += i.calificacion_obtenida
        estandar.calificacion_obtenida = acumulador
        estandar.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_calculo_estandar2:
            acumulador += i.calificacion_obtenida
        estandar2.calificacion_obtenida = acumulador
        estandar2.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_estandares:
            acumulador += i.calificacion_obtenida
        ciclo.calificacion_obtenida = acumulador
        ciclo.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

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
        
        ciclo:(Ciclo) = Ciclo.objects.get(id=2)
        acumulador:(int) = 0 
        #Terminar el otro sub estandar (lista y for)
        for i in lista_items:
            acumulador += i.puntaje_obtenido
        sub_estandar.calificacion_obtenida = acumulador
        sub_estandar.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items2:
            acumulador += i.puntaje_obtenido
        sub_estandar2.calificacion_obtenida = acumulador
        sub_estandar2.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items3:
            acumulador += i.puntaje_obtenido
        sub_estandar3.calificacion_obtenida = acumulador
        sub_estandar3.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items4:
            acumulador += i.puntaje_obtenido
        sub_estandar4.calificacion_obtenida = acumulador
        sub_estandar4.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items5:
            acumulador += i.puntaje_obtenido
        sub_estandar5.calificacion_obtenida = acumulador
        sub_estandar5.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_items6:
            acumulador += i.puntaje_obtenido
        sub_estandar6.calificacion_obtenida = acumulador
        sub_estandar6.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_calculo_estandar:
            acumulador += i.calificacion_obtenida
        estandar.calificacion_obtenida = acumulador
        estandar.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_calculo_estandar2:
            acumulador += i.calificacion_obtenida
        estandar2.calificacion_obtenida = acumulador
        estandar2.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_calculo_estandar3:
            acumulador += i.calificacion_obtenida
        estandar3.calificacion_obtenida = acumulador
        estandar3.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

        for i in lista_estandares:
            acumulador += i.calificacion_obtenida
        ciclo.calificacion_obtenida = acumulador
        ciclo.save(update_fields=['calificacion_obtenida'])
        acumulador = 0

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



class PlanearUsunormal(generic.ListView, LoginRequiredMixin):
    item = ItemEstandar
    context_object_name = 'item_estandar'
    template_name = 'usuarios/usuario/planear.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(PlanearUsunormal, self).get_context_data(**kwargs)
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 1)
        # Add any other variables to the context here
        context['item_estandar2'] = ItemEstandar.objects.filter(fk_sub_estandar = 2)
        return context


class FormatoCreateView(BSModalCreateView):
    template_name = 'usuarios/crear_formato.html'
    model = Formato
    form_class = FormatoModelForm
    success_message = 'Success: Book was created.'
    success_url = "/formatos_admin/"


class FormatosAdmin(generic.ListView, LoginRequiredMixin):
    item = Formato
    template_name = 'usuarios/formatos.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(FormatosAdmin, self).get_context_data(**kwargs)
        context['formatos'] = Formato.objects.all()
        return context


class FormatosUsunormal(generic.ListView, LoginRequiredMixin):
    item = Formato
    template_name = 'usuarios/usuario/formatos.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(FormatosUsunormal, self).get_context_data(**kwargs)
        context['formatos'] = Formato.objects.all()
        return context


class FormatoDeleteView(BSModalDeleteView):
    model = Formato
    template_name = 'usuarios/eliminar_formato.html'
    success_message = 'Success: Formato borrado.'
    success_url = "/formatos_admin/"


class ItemEstadoUpdateView(BSModalUpdateView):
    model = ItemEstandar
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = EstadoItemForm
    success_message = 'Success: Book was updated.'
    success_url = "/planear/"

    def form_valid(self, form, **kwargs):
        self.object = self.get_object()
        item = ItemEstandar.objects.get(id=self.object.pk) # Obtener pk de la url con self.object.pk y self.get_object()
        puntaje_maximo = item.puntaje_maximo
        # Acceder al id de la fk con .id
        estado = item.fk_estado.id
        if form.instance.fk_estado.id == 1:
            item.puntaje_obtenido = puntaje_maximo
            item.save(update_fields=['puntaje_obtenido'])
        elif form.instance.fk_estado.id == 2 or form.instance.fk_estado.id == 3:
            item.puntaje_obtenido = 0
            item.save(update_fields=['puntaje_obtenido'])
        item.fk_estado = form.instance.fk_estado
        item.save(update_fields=['fk_estado_id'])
        return HttpResponseRedirect(self.get_success_url())

class ItemEstadoHacerUpdateView(BSModalUpdateView):
    model = ItemEstandar
    template_name = 'usuarios/cambiar_estado_item.html'
    form_class = EstadoItemForm
    success_message = 'Success: Book was updated.'
    success_url = "/hacer/"

    def form_valid(self, form, **kwargs):
        self.object = self.get_object()
        item = ItemEstandar.objects.get(id=self.object.pk) # Obtener pk de la url con self.object.pk y self.get_object()
        puntaje_maximo = item.puntaje_maximo
        # Acceder al id de la fk con .id
        estado = item.fk_estado.id
        if form.instance.fk_estado.id == 1:
            item.puntaje_obtenido = puntaje_maximo
            item.save(update_fields=['puntaje_obtenido'])
        elif form.instance.fk_estado.id == 2 or form.instance.fk_estado.id == 3:
            item.puntaje_obtenido = 0
            item.save(update_fields=['puntaje_obtenido'])
        item.fk_estado = form.instance.fk_estado
        item.save(update_fields=['fk_estado_id'])
        return HttpResponseRedirect(self.get_success_url())


def verificar(request):
    return render(request, 'usuarios/verificar.html')


def actuar(request):
    return render(request, 'usuarios/actuar.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, Tu cuenta ha sido creada con exito!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'usuarios/register.html', {'form': form})


def login(request):
    if request.method == 'GET':
        context = ''
        return render(request, 'usuarios/login.html', {'context': context})

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            # Validar grupos (roles)
            if user.groups.filter(name='perfiladministrador').exists():
                return redirect('/torta_administrador/')
            elif user.groups.filter(name='perfilgestor').exists():
                return redirect('/torta_gestor/')
            elif user.groups.filter(name='perfilnormal').exists():
                return redirect('/torta_usunormal/')
            else:
                context = {'error': 'Wrong credintials'}  # Agregar mensaje de error
                return render(request, 'usuarios/login.html', {'context': context})
        else:
            context = {'error': 'Wrong credintials'}  # Agregar mensaje de error
            return render(request, 'usuarios/login.html', {'context': context})


def calificar_planear(request):
    item_estandar = request.GET.get('cumple', None)
    response = {
        'respuesta': ItemEstandar.objects.filter(puntaje=item_estandar).exists()
    }
    return JsonResponse(response)



@login_required
def torta_administrador(request):
    return render(request, 'usuarios/torta_administrador.html')


@login_required
def torta_gestor(request):
    return render(request, 'usuarios/torta_gestor.html')


@login_required
def torta_usunormal(request):
    return render(request, 'usuarios/torta_usunormal.html')
