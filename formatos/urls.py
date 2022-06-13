
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Formatos
    path('registrar_formato/', login_required(views.FormatoCreateView.as_view()), name='registrar_formato'),
    path('formatos_admin/', views.FormatosAdmin.as_view(), name='formatos_admin'),
    path('formatos_usunormal/', views.FormatosUsunormal.as_view(), name='formatos_usunormal'),
    path('<int:pk>/eliminar_formato', views.FormatoDeleteView.as_view(), name='eliminar_formato'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )