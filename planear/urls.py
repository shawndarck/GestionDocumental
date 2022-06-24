
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Login required permite proteger la vista a nivel de class vased views
    path('calificar_planear/', views.calificar_planear, name='calificar_planear'),

    # Evidencias
    path('registrar_evidencia_planear/<int:pk>', login_required(views.EvidenciaPlanearCreateView.as_view()), name='registrar_evidencia_planear'),
    path('<int:pk>/eliminar_evidencia_planear', views.EvidenciaPlanearDeleteView.as_view(), name='eliminar_evidencia_planear'),

    # Redirecciones
    path('estado_item/<int:pk>', login_required(views.ItemEstadoUpdateView.as_view()), name='estado_item'),
    path('planear/', login_required(views.Planear.as_view()), name='planear'),

    path('planear_usuario/', login_required(views.PlanearUsunormal.as_view()), name='planear_usuario'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )