
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    # path('', views.login, name='login'),
    # path('register/', views.register, name='register'),
    path('sidebar/', views.sidebar, name='sidebar'),
    # path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('planear/', views.planear, name="planear"),
    path('', auth_view.LoginView.as_view(template_name='usuarios/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
]