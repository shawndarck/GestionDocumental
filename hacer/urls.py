
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<int:pk>/eliminar_evidencia', login_required(views.EvidenciaHacerDeleteView.as_view()), name='eliminar_evidencia'),

    path('estado_item_hacer/<int:pk>', login_required(views.ItemEstadoHacerUpdateView.as_view()), name='estado_item_hacer'),

    path('hacer_usuario/', login_required(views.HacerUsunormal.as_view()), name='hacer_usuario'),

    path('hacer/', login_required(views.Hacer.as_view()), name="hacer"),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )