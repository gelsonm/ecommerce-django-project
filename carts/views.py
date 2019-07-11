from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from .models import Cart
from django.contrib import messages

def view_cart(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "cart.html",{'cart':cart_obj})


def add_to_cart(request, id):
    #quantity_input= request.POST.get('quantity')
    if id is not None:
        try:
            product_obj = Product.objects.get(id=id)
        except Product.DoesNotExist:
            messages.error(request, "Product not available anymore!")
            return redirect("cart.html")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all(): 
            cart_obj.products.remove(product_obj)
            added = False
        else:
            cart_obj.products.add(product_obj) 
            added = True
            messages.success(request, "Product added succesfully to cart!")
        request.session['cart_items'] = cart_obj.products.count()
        
    return redirect(reverse('index'))

def delete_from_cart(request, id):
    if id is not None:
        try:
            product_obj = Product.objects.get(id=id)
        except Product.DoesNotExist:
            messages.error(request, "Product not available anymore!")
            return redirect("cart.html")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all(): 
            cart_obj.products.remove(product_obj)
            added = False
            messages.success(request, "Product removed from cart!")
        else:
            messages.error(request, "Product already deleted!")
    return redirect(reverse('index'))

'''
def cart_update(request, id):
    product_id = id
    quantity_input= request.POST.get('quantity')

    if product_id is not None:            
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        Entry.objects.create(cart=cart_obj, product=product_obj, quantity=quantity_input)
        cart_obj.products.add(product_obj)            
        added = True
        request.session['cart_items'] = cart_obj.products.count()        
    return render(request, "cart.html",{'cart':cart_obj})
'''

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html",{"cart":cart_obj})
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart    
    return redirect(reverse('index'))


def adjust_cart(request, id):
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart    
    return redirect(reverse('view_cart'))
