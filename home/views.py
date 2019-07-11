from django.shortcuts import render
from products.models import Product
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def home_view(request):
    featured = Product.objects.all().featured()
    return render(request,"index.html",{'featured':featured,'text':'Featured'})

def about(request):
    return render(request,"about.html")

