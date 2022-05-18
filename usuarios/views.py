from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from ciclo_phva.models import ItemEstandar, Evidencia
from django.conf import settings


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
    if request.method == "POST":
        # Obtención de los datos del formulario
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        content_type = uploadedFile.content_type.split('/')[1]
        if content_type in CONTENT_TYPES:
            if uploadedFile.size > int(MAX_UPLOAD_SIZE):
                raise ValidationError('El archivo supera los dos 2,5 MB Intenta nuevamente')
        else:
            raise ValidationError('Formato de archivo no válido')
        
        # Guarda la información en la base de datos
        document = Evidencia(
            nombre_evidencia = fileTitle,
            nombre_formato = fileTitle,
            formato = uploadedFile
        )
        document.save()

    documents = Evidencia.objects.all()
    return render(request, "usuarios/index.html", context = {"files": documents})


class Planear(generic.ListView):
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


@login_required()
def sidebar(request):
    return render(request, 'usuarios/sidebar.html')
