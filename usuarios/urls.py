
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Login required permite proteger la vista a nivel de class vased views
    path('calificar_planear/', views.calificar_planear, name='calificar_planear'),

    # Formatos
    path('registrar_formato/', views.FormatoCreateView.as_view(), name='registrar_formato'),
    path('formatos_admin/', views.FormatosAdmin.as_view(), name='formatos_admin'),
    path('formatos_usunormal/', views.FormatosUsunormal.as_view(), name='formatos_usunormal'),
    path('<int:pk>/eliminar_formato', views.FormatoDeleteView.as_view(), name='eliminar_formato'),
    # Evidencias
    path('registrar_evidencia/<int:pk>', login_required(views.EvidenciaCreateView.as_view()), name='registrar_evidencia'),
    path('leer_evidencias/<int:fk>', login_required(views.EvidenciaReadView.as_view()), name='leer_evidencias'),
    path('index/',views.index,name="index"),
    path('register/', views.register, name='register'),
    # Redirecciones
    path('estado_item/<int:pk>', login_required(views.ItemEstadoUpdateView.as_view()), name='estado_item'),
    path('estado_item_hacer/<int:pk>', login_required(views.ItemEstadoHacerUpdateView.as_view()), name='estado_item_hacer'),
    path('planear/', login_required(views.Planear.as_view()), name='planear'),
    path('torta_administrador/', login_required(views.torta_administrador), name='torta_administrador'),
    path('torta_gestor/', login_required(views.torta_gestor), name='torta_gestor'),
    path('torta_usunormal/', login_required(views.torta_usunormal), name='torta_usunormal'),

    path('planear_usunormal/', login_required(views.PlanearUsunormal.as_view()), name='planear_usunormal'),
    path('hacer/', login_required(views.Hacer.as_view()), name="hacer"),
    path('verificar/', views.verificar, name="verificar"),
    path('actuar/', views.actuar, name="actuar"),
    path('', views.login, name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )