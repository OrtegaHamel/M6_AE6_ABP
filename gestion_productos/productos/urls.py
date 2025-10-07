# productos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
