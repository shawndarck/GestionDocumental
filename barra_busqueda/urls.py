
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('busqueda/', login_required(views.barra_busqueda), name="busqueda")
]
# urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
