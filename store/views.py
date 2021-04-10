from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'store/home.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products':products})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/detail.html', {'product': product})
