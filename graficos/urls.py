from django.urls import include, path
from graficos import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # Grafico estadistico
    path('grafico_phva/', login_required(views.bar_chart_phva), name='grafico_phva'),
    path('filtro_pruebas_covid/', login_required(views.PruebasCovidFilterView.as_view()), name='filtro_pruebas_covid'),
    path('filtro_epidemiologia/', login_required(views.EpidemiologiaFilterView.as_view()), name='filtro_epidemiologia'),
    path('filtro_incapacidades/', login_required(views.IncapacidadesCovidFilterView.as_view()), name='filtro_incapacidades'),
    path('filtro_incidencias/', login_required(views.IncidenciaFilterView.as_view()), name='filtro_incidencias'),
    path('filtro_tipo_caso_sospechosos/', login_required(views.TipoCasoSospechosoFilterView.as_view()), name='filtro_tipo_caso_sospechosos'),
    path('filtro_casos_cliente/', login_required(views.CasosClienteFilterView.as_view()), name='filtro_casos_cliente'),
    #Gráficos
    path('grafico_pruebas_covid/', login_required(views.bar_chart_pruebas_covid), name='grafico_pruebas_covid'),
    path('grafico_epidemiologia/', login_required(views.bar_chart_epidemiologia), name='grafico_epidemiologia'),
    path('grafico_incapacidades/', login_required(views.bar_chart_incapacidades_covid), name='grafico_incapacidades'),
    path('grafico_incidencias/', login_required(views.bar_chart_incidencia), name='grafico_incidencias'),
    path('grafico_tipo_caso_sospechosos/', login_required(views.bar_chart_tipo_caso_sospechoso), name='grafico_tipo_caso_sospechosos'),
    path('grafico_casos_cliente/', login_required(views.bar_chart_casos_clientes), name='grafico_casos_cliente'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )