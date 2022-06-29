
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('torta_administrador/', login_required(views.TortaAdministrador.as_view()), name='torta_administrador'),
    path('torta_gestor/', login_required(views.torta_gestor), name='torta_gestor'),
    path('torta_usunormal/', login_required(views.torta_usunormal), name='torta_usunormal'),
    path('', views.login, name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),

    # Gestión de usuarios
    path('gestion_usuarios/', login_required(views.GestionUsuarios.as_view()), name='gestion_usuarios'),
    path('estado_usuarios/<int:pk>', login_required(views.CambiaEstadoUsuario.as_view()), name='estado_usuarios'),
    path('registrar_usuario/', login_required(views.RegistrarUsuario.as_view()), name='registrar_usuario'),
    path('registrar_administrador/', login_required(views.RegistrarAdministrador.as_view()), name='registrar_administrador'),
    path('registrar_gestor/', login_required(views.RegistrarGestor.as_view()), name='registrar_gestor'),
    path('verification/', include('verify_email.urls')),
    path('perfil/', login_required(views.PerfilDetailView.as_view()), name='perfil'),
    path('cambiar_clave/<int:pk>', login_required(views.PasswordUpdateView.as_view()), name='cambiar_clave'),
    # path('verification/', include('verify_email')),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )