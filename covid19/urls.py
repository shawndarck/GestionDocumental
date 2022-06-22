
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Redirecciones
    path('covid19/', login_required(views.covid19), name='covid19'),
    path('pruebas_covid/', login_required(views.PruebasCovidTabla.as_view()), name='pruebas_covid'),
    path('leer_anuales/', login_required(views.LeerAnualReadView.as_view()), name='leer_anuales'),
    path('crear_anual/', login_required(views.RegistroAnualCreateView.as_view()), name='crear_anual'),
    path('<int:pk>/eliminar_anual', views.RegistroAnualDeleteView.as_view(), name='eliminar_anual'),
    path('editar_prueba_covid/<int:pk>', views.PruebasCovidUpdateView.as_view(), name='editar_prueba_covid'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )