# from django.views import ListView
from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def featured_products(request):
    products = Product.objects.all().featured()
    return render(request, "product-list.html", {"products": products,"text":'Featured Products'})

def all_products(request):
    products = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 5)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "product-list.html", {"products": products,"text":'All'})

def product_detail(request,id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product-detail.html", {"product": product})

