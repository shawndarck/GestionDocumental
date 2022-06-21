
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('reportes/', include('reportes.urls')),
    path('graficos/', include('graficos.urls')),
    path('evidencias/', include('evidencias.urls')),
    path('planear/', include('planear.urls')),
    path('hacer/', include('hacer.urls')),
    path('verificar/', include('verificar.urls')),
    path('actuar/', include('actuar.urls')),
    path('', include('accesos.urls')),
    path('formatos/', include('formatos.urls')),
    path('covid19/', include('covid19.urls')),
]
# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
