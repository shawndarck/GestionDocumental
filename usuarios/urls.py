
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('calificar_planear/', views.calificar_planear, name='calificar_planear'),

    path('<int:pk>/eliminar_formato', views.FormatoDeleteView.as_view(), name='eliminar_formato'),
    path('torta_administrador/', login_required(views.torta_administrador), name='torta_administrador'),
    path('torta_gestor/', login_required(views.torta_gestor), name='torta_gestor'),
    path('torta_usunormal/', login_required(views.torta_usunormal), name='torta_usunormal'),
    path('registrar_evidencia/<int:pk>', login_required(views.EvidenciaCreateView.as_view()), name='registrar_evidencia'),
    path('registrar_formato/', views.FormatoCreateView.as_view(), name='registrar_formato'),
    # Formatos
    path('formatos_admin/', views.FormatosAdmin.as_view(), name='formatos_admin'),
    path('formatos_usunormal/', views.FormatosUsunormal.as_view(), name='formatos_usunormal'),
    path('leer_evidencias/<int:fk>', login_required(views.EvidenciaReadView.as_view()), name='leer_evidencias'),
    path('index/',views.index,name="index"),
    path('register/', views.register, name='register'),
    # Login required permite proteger la vista a nivel de class vased views
    path('planear/', login_required(views.Planear.as_view()), name='planear'),

    path('planear_usunormal/', login_required(views.PlanearUsunormal.as_view()), name='planear_usunormal'),
    path('hacer/', views.hacer, name="hacer"),
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