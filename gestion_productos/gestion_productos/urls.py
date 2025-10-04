from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('denegado/', TemplateView.as_view(template_name='denegado.html'), name='denegado'),
]
