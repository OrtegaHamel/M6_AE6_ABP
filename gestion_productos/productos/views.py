from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

@login_required
@permission_required('productos.add_producto', login_url='denegado')
def lista_productos(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/lista_productos.html', {'productos': productos, 'form': form})

@login_required
@permission_required('productos.delete_producto', login_url='denegado')
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/confirmar_eliminar.html', {'producto': producto})

def home(request):
    return render(request, 'home.html')
