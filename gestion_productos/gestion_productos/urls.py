from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from gestion_productos import views  # Importa desde el paquete gestion_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('denegado/', TemplateView.as_view(template_name='registration/denegado.html'), name='denegado'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('productos/', include('productos.urls')),
]
