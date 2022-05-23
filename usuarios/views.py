from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login
from django.urls import reverse_lazy
from django.views import generic
from ciclo_phva.models import ItemEstandar, Evidencia
from django.conf import settings
from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import EvidenciaModelForm

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
    template_name = 'usuarios/crear_evidencia.html'
    model = ItemEstandar
    form_class = EvidenciaModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('planear')

    def form_valid(self, form):
        form.instance.fk_item_estandar_id = self.kwargs.get('pk')
        return super(EvidenciaCreateView, self).form_valid(form)

    # def dispatch(self, request, *args, **kwargs):
    #     """
    #     Overridden so we can make sure the `Ipsum` instance exists
    #     before going any further.
    #     """
    #     self.evidencia = get_object_or_404(Evidencia, pk=kwargs['pk'])
    #     return super().dispatch(request, *args, **kwargs)

    # def form_valid(self, form_class):
    #     """
    #     Overridden to add the ipsum relation to the `Lorem` instance.
    #     """
    #     form_class.instance.evidencia = self.evidencia
    #     return super().form_valid(form_class)


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
        context['item_estandar1'] = ItemEstandar.objects.filter(fk_sub_estandar = 1)
        # Add any other variables to the context here
        context['item_estandar2'] = ItemEstandar.objects.filter(fk_sub_estandar = 2)
        return context


def hacer(request):
    return render(request, 'usuarios/hacer.html')


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
                return render(request, 'usuarios/torta_administrador.html')
            elif user.groups.filter(name='perfilgestor').exists():
                # Url de ejemplo
                return render(request, 'usuarios/torta_gestor.html')
            elif user.groups.filter(name='perfilnormal').exists():
                return render(request, 'usuarios/torta_usunormal.html')
            else:
                context = {'error': 'Wrong credintials'}  # Agregar mensaje de error
                return render(request, 'usuarios/login.html', {'context': context})
        else:
            context = {'error': 'Wrong credintials'}  # Agregar mensaje de error
            return render(request, 'usuarios/login.html', {'context': context})


@login_required
def torta_administrador(request):
    return render(request, 'usuarios/torta_administrador.html')

@login_required
def torta_gestor(request):
    return render(request, 'usuarios/torta_gestor.html')

@login_required
def torta_usunormal(request):
    return render(request, 'usuarios/torta_usunormal.html')
