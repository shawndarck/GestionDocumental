
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<int:pk>/eliminar_evidencia_actuar', views.EvidenciaActuarDeleteView.as_view(), name='eliminar_evidencia_actuar'),

    path('estado_item_actuar/<int:pk>', login_required(views.ItemEstadoActuarUpdateView.as_view()), name='estado_item_actuar'),

    path('actuar_usuario/', login_required(views.ActuarUsunormal.as_view()), name='actuar_usuario'),

    path('actuar/', login_required(views.Actuar.as_view()), name="actuar"),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )