from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('gestion_ambiental', login_required(views.GestionAmbientalListView.as_view()), name='gestion_ambiental'),
    path('registrar_evidencia_gestion_ambiental/<int:pk>', login_required(views.EvidenciaGestionAmbientalCreateView.as_view()), name='registrar_evidencia_gestion_ambiental'),
    path('leer_evidencias_gestion_ambiental/<int:fk>', login_required(views.EvidenciaGestionAmbientalReadView.as_view()), name='leer_evidencias_gestion_ambiental'),
    path('<int:pk>/eliminar_evidencia', login_required(views.EvidenciaGestionAmbientalDeleteView.as_view()), name='eliminar_evidencia'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )