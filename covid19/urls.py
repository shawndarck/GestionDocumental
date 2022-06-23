
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
    path('epidemologia/', login_required(views.EpidemiologiaTabla.as_view()), name='epidemologia'),
    path('editar_epidemologia/<int:pk>', views.EpidemiologiaUpdateView.as_view(), name='editar_epidemologia'),
    # Incapacidades
    path('incapacidades/', login_required(views.IncapacidadesCovidTabla.as_view()), name='incapacidades'),
    path('editar_incapacidad/<int:pk>', login_required(views.IncapacidadesCovidUpdateView.as_view()), name='editar_incapacidad'),
    # Incidencias
    path('incidencias/', login_required(views.IncidenciasTabla.as_view()), name='incidencias'),
    path('editar_incidencia/<int:pk>', login_required(views.IncidenciasUpdateView.as_view()), name='editar_incidencia'),
    # Tipos de caso sospechoso
    path('tipo_caso_sospechoso/', login_required(views.TipoCasoSospechosoTabla.as_view()), name='tipo_caso_sospechoso'),
    path('editar_tipo_incidencia/<int:pk>', login_required(views.TipoCasoSospechosoUpdateView.as_view()), name='editar_tipo_incidencia'),
    # Casos por cliente
    path('casos_cliente/', login_required(views.CasosClienteTabla.as_view()), name='casos_cliente'),
    path('registrar_caso_cliente/', login_required(views.CasosClienteCreateView.as_view()), name='registrar_caso_cliente'),
    path('editar_casos_cliente/<int:pk>', login_required(views.CasosClienteUpdateView.as_view()), name='editar_casos_cliente'),
    path('leer_anuales_cliente/<int:pk>', login_required(views.ClienteAnualesReadView.as_view()), name='leer_anuales_cliente'),
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