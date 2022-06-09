
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Login required permite proteger la vista a nivel de class vased views
    path('calificar_planear/', views.calificar_planear, name='calificar_planear'),

    # Formatos
    path('registrar_formato/', login_required(views.FormatoCreateView.as_view()), name='registrar_formato'),
    path('formatos_admin/', views.FormatosAdmin.as_view(), name='formatos_admin'),
    path('formatos_usunormal/', views.FormatosUsunormal.as_view(), name='formatos_usunormal'),
    path('<int:pk>/eliminar_formato', views.FormatoDeleteView.as_view(), name='eliminar_formato'),
    path('<int:pk>/eliminar_evidencia', views.EvidenciaPlanearDeleteView.as_view(), name='eliminar_evidencia'),
    # Evidencias
    path('registrar_evidencia_planear/<int:pk>', login_required(views.EvidenciaPlanearCreateView.as_view()), name='registrar_evidencia_planear'),
    path('registrar_evidencia_hacer/<int:pk>', login_required(views.EvidenciaHacerCreateView.as_view()), name='registrar_evidencia_hacer'),
    path('registrar_evidencia_verificar/<int:pk>', login_required(views.EvidenciaVerificarCreateView.as_view()), name='registrar_evidencia_verificar'),
    path('registrar_evidencia_actuar/<int:pk>', login_required(views.EvidenciaActuarCreateView.as_view()), name='registrar_evidencia_actuar'),
    path('leer_evidencias/<int:fk>', login_required(views.EvidenciaReadView.as_view()), name='leer_evidencias'),

    # Redirecciones
    path('estado_item/<int:pk>', login_required(views.ItemEstadoUpdateView.as_view()), name='estado_item'),
    path('estado_item_hacer/<int:pk>', login_required(views.ItemEstadoHacerUpdateView.as_view()), name='estado_item_hacer'),
    path('estado_item_verificar/<int:pk>', login_required(views.ItemEstadoVerificarUpdateView.as_view()), name='estado_item_verificar'),
    path('estado_item_actuar/<int:pk>', login_required(views.ItemEstadoActuarUpdateView.as_view()), name='estado_item_actuar'),
    path('planear/', login_required(views.Planear.as_view()), name='planear'),
    path('torta_administrador/', login_required(views.TortaAdministrador.as_view()), name='torta_administrador'),
    path('torta_gestor/', login_required(views.torta_gestor), name='torta_gestor'),
    path('torta_usunormal/', login_required(views.torta_usunormal), name='torta_usunormal'),
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
    path('planear_usuario/', login_required(views.PlanearUsunormal.as_view()), name='planear_usuario'),
    path('hacer_usuario/', login_required(views.HacerUsunormal.as_view()), name='hacer_usuario'),
    path('verificar_usuario/', login_required(views.VerificarUsunormal.as_view()), name='verificar_usuario'),
    path('actuar_usuario/', login_required(views.ActuarUsunormal.as_view()), name='actuar_usuario'),
    path('leer_evidencias_usuario/<int:fk>', login_required(views.EvidenciaUsuarioReadView.as_view()), name='leer_evidencias_usuario'),
    path('eliminar_acceso/<int:pk>/<int:id>', login_required(views.QuitarAcceso.as_view()), name='eliminar_acceso'),

    path('hacer/', login_required(views.Hacer.as_view()), name="hacer"),
    path('verificar/', login_required(views.Verificar.as_view()), name="verificar"),
    path('actuar/', login_required(views.Actuar.as_view()), name="actuar"),
    path('', views.login, name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),

    # Gestión de usuarios
    path('gestion_usuarios/', login_required(views.GestionUsuarios.as_view()), name='gestion_usuarios'),
    path('estado_usuarios/<int:pk>', login_required(views.CambiaEstadoUsuario.as_view()), name='estado_usuarios'),
    path('registrar_usuario/', login_required(views.RegistrarUsuario.as_view()), name='registrar_usuario'),
    path('registrar_administrador/', login_required(views.RegistrarAdministrador.as_view()), name='registrar_administrador'),
    path('verification/', include('verify_email.urls')),
    path('perfil/', login_required(views.PerfilDetailView.as_view()), name='perfil'),
    path('cambiar_clave/<int:pk>', login_required(views.PasswordUpdateView.as_view()), name='cambiar_clave'),
    # path('verification/', include('verify_email')),

    # Grafico estadistico
    path('grafico_phva/', login_required(views.bar_chart_phva), name='grafico_phva'),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )