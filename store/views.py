from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'store/home.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products':products})
