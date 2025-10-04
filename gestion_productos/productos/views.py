from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Producto

class ProductoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('admin:index')
    permission_required = 'productos.delete_producto'
    raise_exception = False  # Redirige a la página de login si no tiene permiso
    login_url = '/denegado/'  # Redirige a acceso denegado
