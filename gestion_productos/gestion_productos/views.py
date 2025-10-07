# gestion_productos/gestion_productos/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
