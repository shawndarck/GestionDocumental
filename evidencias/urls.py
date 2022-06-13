
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Evidencias
    path('registrar_evidencia_planear/<int:pk>', login_required(views.EvidenciaPlanearCreateView.as_view()), name='registrar_evidencia_planear'),
    path('registrar_evidencia_hacer/<int:pk>', login_required(views.EvidenciaHacerCreateView.as_view()), name='registrar_evidencia_hacer'),
    path('registrar_evidencia_verificar/<int:pk>', login_required(views.EvidenciaVerificarCreateView.as_view()), name='registrar_evidencia_verificar'),
    path('registrar_evidencia_actuar/<int:pk>', login_required(views.EvidenciaActuarCreateView.as_view()), name='registrar_evidencia_actuar'),
    path('leer_evidencias/<int:fk>', login_required(views.EvidenciaReadView.as_view()), name='leer_evidencias'),
    path('leer_evidencias_usuario/<int:fk>', login_required(views.EvidenciaUsuarioReadView.as_view()), name='leer_evidencias_usuario'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )