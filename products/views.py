# from django.views import ListView
from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "product-list.html", {"products": products})

def product_detail(request,id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product-detail.html", {"product": product})

