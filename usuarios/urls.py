
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('', views.login, name='login'),
    # path('register/', views.register, name='register'),
    # path('read/<int:pk>', views.BookReadView.as_view(), name='read_book'),
    path('torta_administrador/', views.torta_administrador, name='torta_administrador'),
    path('torta_gestor/', views.torta_administrador, name='torta_gestor'),
    path('torta_usunormal/', views.torta_administrador, name='torta_usunormal'),
    path('index/',views.index,name="index"),
    path('registrar_evidencia/<int:pk>', views.EvidenciaCreateView.as_view(), name='registrar_evidencia'),
    path('leer_evidencias/<int:fk>', views.EvidenciaReadView.as_view(), name='leer_evidencias'),
    # path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    # Login required permite proteger la vista a nivel de class vased views
    path('planear/', login_required(views.Planear.as_view()), name='planear'),
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