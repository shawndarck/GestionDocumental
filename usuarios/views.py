import random
from types import NoneType
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as dj_login, logout
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.models import Group

from usuarios.models import Usuario 
from ciclo_phva.models import (
    ItemEstandar,
    Evidencia,
    Formato,
    SubEstandar,
    Estandar,
    Ciclo,
    Phva,
)

from ciclo_phva.forms import EstadoItemForm

from .forms import (
    UsuarioForm,
    AdminForm,
    CambiarParsswordForm,
    LoginForm,
)

from bootstrap_modal_forms.generic import BSModalCreateView
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)


class RegistrarAdministrador(BSModalCreateView):
    template_name = 'usuarios/crear_administrador.html'
    form_class = AdminForm
    success_message = 'Success: Usuario creado.'
    success_url = reverse_lazy('gestion_usuarios')
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = Usuario.objects.make_random_password()
            # Valida correo cinte
            if "@grupocinte.com" in username:
                nuevo_administrador = Usuario(
                    username=form.cleaned_data.get('username'),
                    es_administrador=True
                )
                nuevo_administrador.set_password(password)
                nuevo_administrador.save()
                # Envía mail
                send_mail(
                    subject=username,
                    message='Has sido registrado en el sistema de gestión documental SST, tu clave es: ' + password,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[username],
                )
                messages.success(request, "Usuario creado correctamente, clave enviada al correo")
                return HttpResponseRedirect(reverse_lazy('gestion_usuarios'))
            else:
                messages.success(request, "Usuario duplicado o dominio de cinte incorrecto @grupocinte.com")
                return HttpResponseRedirect(reverse_lazy('gestion_usuarios'))
        else:
            return HttpResponseRedirect(reverse_lazy('gestion_usuarios'))


class RegistrarUsuario(BSModalCreateView):
    template_name = 'usuarios/crear_usuario.html'
    form_class = UsuarioForm
    success_message = 'Success: Usuario creado.'
    success_url = reverse_lazy('gestion_usuarios')


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = Usuario.objects.make_random_password()
            # Valida correo cinte
            if "@grupocinte.com" in username:
                nuevo_usuario = Usuario(
                    username=form.cleaned_data.get('username'),
                    es_usuario=True
                )
                nuevo_usuario.set_password(password)
                nuevo_usuario.save()
                # Envía mail
                send_mail(
                    subject=username,
                    message='Has sido registrado en el sistema de gestión documental SST, tu clave es: ' + password,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[username],
                )
                messages.success(request, "Usuario creado correctamente, clave enviada al correo")
                return HttpResponseRedirect(reverse_lazy('gestion_usuarios'))
            else:
                messages.success(request, "Usuario duplicado o dominio de cinte incorrecto @grupocinte.com")
                return HttpResponseRedirect(reverse_lazy('gestion_usuarios'))
        else:
            return HttpResponseRedirect(reverse_lazy('gestion_usuarios'))


class GestionUsuarios(generic.ListView, LoginRequiredMixin):
    item = Usuario
    context_object_name = 'usuarios'
    template_name = 'usuarios/gestion_usuarios.html'
    success_url = reverse_lazy('gestion_usuarios')

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if self.success_url:
            url = self.success_url.format(**self.object.__dict__)
        else:
            url = self.object.get_absolute_url()
        return url

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(GestionUsuarios, self).get_context_data(**kwargs)        
        # Contextos individuales (Objeto)
        context['usuarios'] = Usuario.objects.all()
        return context


class PerfilDetailView(generic.ListView, LoginRequiredMixin):
    item = Usuario
    context_object_name = 'usuario'
    template_name = 'usuarios/perfil.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(PerfilDetailView, self).get_context_data(**kwargs)
        context['usuario'] = Usuario.objects.get(id=self.request.user.id)

class PasswordUpdateView(BSModalUpdateView):
    model = Usuario
    template_name = 'usuarios/actualizar_clave.html'
    form_class = CambiarParsswordForm
    success_message = 'Success: Clave cambiada.'
    success_url = reverse_lazy('perfil')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = Usuario.objects.filter(id=request.user.id)
            if user.exists():
                user = user.first()
                user.set_password(form.cleaned_data.get('password1'))
                user.save()
                logout(request)
                return redirect(self.success_url)
            return redirect(self.success_url)
        else:
            form = self.form_class(request.POST)
            return render(request, self.template_name, {'form': form})


def login(request):

    if request.method == 'GET':
        form = LoginForm(request.POST)
        context = ''
        return render(request, 'usuarios/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # validador = RegexValidator(r'(\W|^)[\w.\-]{0,25}@(grupocinte)\.com(\W|$)', Fa)
        # validador(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            # Agregar otro if para verificar el estado y validacion de usuario
            # if user.is_active & user.es_valido:
            # Validar grupos (roles)
            if user.groups.filter(name='perfilnormal').exists() & user.es_valido & user.es_usuario:
                return redirect('/torta_usunormal/')
            elif user.groups.filter(name='perfiladministrador').exists() & user.es_valido & user.es_administrador:
                return redirect('/torta_administrador/')
            elif user.groups.filter(name='perfilgestor').exists() & user.es_valido & user.es_gestor:
                return redirect('/torta_gestor/')
            # Si el usuario no esta validado y no tiene grupo se le asigna un grupo y se activa
            elif user.es_usuario == True:
                Group.objects.get(name='perfilnormal').user_set.add(user)
                return redirect('/torta_usunormal/')
            elif user.es_administrador == True:
                Group.objects.get(name='perfiladministrador').user_set.add(user)
                return redirect('/torta_administrador/')
            else:
                context = {'error': messages.success(request, "Usuario desactivado! contacte con un administrador")}  # Agregar mensaje de error
                return render(request, 'usuarios/login.html', {'context': context})
        else:
            context = {'error': messages.success(request, "Correo o clave incorrectos")}  # Agregar mensaje de error
            return render(request, 'usuarios/login.html', {'context': context})


class TortaAdministrador(generic.ListView, LoginRequiredMixin):
    item = Ciclo
    context_object_name = 'item'
    template_name = 'usuarios/torta_administrador.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        context = super(TortaAdministrador, self).get_context_data(**kwargs)
        context['planear'] = Ciclo.objects.get(id = 1)
        context['hacer'] = Ciclo.objects.get(id = 2)
        context['verificar'] = Ciclo.objects.get(id = 3)
        context['actuar'] = Ciclo.objects.get(id = 4)
        context['phva'] = Phva.objects.get(id = 1)
        return context


class CambiaEstadoUsuario(generic.ListView, LoginRequiredMixin):
    item = Usuario
    context_object_name = 'usuario'
    template_name = 'usuarios/gestion_usuarios.html'
    http_method_names = ['get']

    def get_queryset(self):
        pass

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            messages.success(self.request, "Se a cambiado el estado correctamente")
            return redirect(self.success_url)
        else:
            return HttpResponseRedirect(reverse_lazy('gestion_usuarios'))

    def get_context_data(self, **kwargs):
        # Prerrequisito
        context = super(CambiaEstadoUsuario, self).get_context_data(**kwargs) 
        usu=Usuario.objects.get(id=self.kwargs.get('pk'))
        if usu.is_active == True:
            usu.is_active = False
        else:
            usu.is_active = True
        usu.save(update_fields=['is_active'])
        # Contextos individuales (Objeto)
        messages.success(self.request, "Se a cambiado el estado correctamente")
        context['usuarios'] = Usuario.objects.all()
        return context


@login_required
def torta_gestor(request):
    return render(request, 'usuarios/torta_gestor.html')


@login_required
def torta_usunormal(request):
    return render(request, 'usuarios/torta_usunormal.html')