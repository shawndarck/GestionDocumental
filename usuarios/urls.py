
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('sidebar/', views.sidebar, name='sidebar'),
    path('index/',views.index,name="index"),
    # path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('planear/', views.Planear.as_view(), name='planear'),
    path('hacer/', views.hacer, name="hacer"),
    path('verificar/', views.verificar, name="verificar"),
    path('actuar/', views.actuar, name="actuar"),
    path('', auth_view.LoginView.as_view(template_name='usuarios/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )