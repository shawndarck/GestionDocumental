
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<int:pk>/eliminar_evidencia', views.EvidenciaVerificarDeleteView.as_view(), name='eliminar_evidencia'),

    path('estado_item_verificar/<int:pk>', login_required(views.ItemEstadoVerificarUpdateView.as_view()), name='estado_item_verificar'),

    path('verificar_usuario/', login_required(views.VerificarUsunormal.as_view()), name='verificar_usuario'),

    path('verificar/', login_required(views.Verificar.as_view()), name="verificar"),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )