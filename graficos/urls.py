from django.urls import include, path
from graficos import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # Grafico estadistico
    path('grafico_phva/', login_required(views.bar_chart_phva), name='grafico_phva'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )