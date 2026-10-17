from django.shortcuts import render
from .models import Product, Reservation
from .models import Apartament, Reservation

def  home(request):
    apartaments =  Product.objects.all()
    return render(request, 'home.html', {'apartments': apartaments})

def apartament_page(request, apartament_id):
    apartament = Product.objects.get(id=apartament_id)
    return render(request, 'apartament_page.html', {'apartament': apartament})