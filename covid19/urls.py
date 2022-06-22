
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Redirecciones
    # Redirección pagina principal
    path('covid19/', login_required(views.covid19), name='covid19'),
    # Pruebas covid
    path('pruebas_covid/', login_required(views.PruebasCovidTabla.as_view()), name='pruebas_covid'),
    path('editar_prueba_covid/<int:pk>', views.PruebasCovidUpdateView.as_view(), name='editar_prueba_covid'),
    # Epidemologia
    path('epidemologia/', login_required(views.EpidemologiaTabla.as_view()), name='epidemologia'),
    path('editar_epidemologia/<int:pk>', views.EpidemologiaUpdateView.as_view(), name='editar_epidemologia'),
    # Gestión de años
    path('leer_anuales/', login_required(views.LeerAnualReadView.as_view()), name='leer_anuales'),
    path('crear_anual/', login_required(views.RegistroAnualCreateView.as_view()), name='crear_anual'),
    path('<int:pk>/eliminar_anual', views.RegistroAnualDeleteView.as_view(), name='eliminar_anual'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )