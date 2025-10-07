from django.contrib import admin
from django.shortcuts import redirect
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('productos.delete_producto')

    def delete_view(self, request, object_id, extra_context=None):
        if not self.has_delete_permission(request):
            return redirect('denegado')
        return super().delete_view(request, object_id, extra_context)

admin.site.register(Producto, ProductoAdmin)


