
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #Permisos
    path('permisos_evidencias/', login_required(views.GestionPermisosEvidencias.as_view()), name='permisos_evidencias'),
    path('accesos_planear/', login_required(views.AccesosPlanear.as_view()), name='accesos_planear'),
    path('accesos_hacer/', login_required(views.AccesosHacer.as_view()), name='accesos_hacer'),
    path('accesos_verificar/', login_required(views.AccesosVerificar.as_view()), name='accesos_verificar'),
    path('accesos_actuar/', login_required(views.AccesosActuar.as_view()), name='accesos_actuar'),
    path('permisos_usuarios_planear/<int:pk>', login_required(views.PermisosPlanearCreateView.as_view()), name='permisos_usuarios_planear'),
    path('permisos_usuarios_hacer/<int:pk>', login_required(views.PermisosHacerCreateView.as_view()), name='permisos_usuarios_hacer'),
    path('permisos_usuarios_verificar/<int:pk>', login_required(views.PermisosVerificarCreateView.as_view()), name='permisos_usuarios_verificar'),
    path('permisos_usuarios_actuar/<int:pk>', login_required(views.PermisosActuarCreateView.as_view()), name='permisos_usuarios_actuar'),
    path('leer_permisos/<int:pk>', login_required(views.PermisosReadView.as_view()), name='leer_permisos'),
    path('eliminar_acceso/<int:pk>/<int:id>', login_required(views.QuitarAcceso.as_view()), name='eliminar_acceso'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )