from django.shortcuts import render
from products.models import Product
from django.db.models import Q

def do_search(request):
    query=request.GET['q']
    lookups = (Q(title__icontains=query)| 
                  Q(description__icontains=query)|
                  Q(price__icontains=query)
                  )
    products=Product.objects.filter(lookups).distinct()
    #products = Product.objects.filter(title__icontains=request.GET['q'])
    return render(request, "product-list.html", {"products": products,"text":'Search Results'})