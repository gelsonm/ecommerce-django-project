from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem,Order
from django.conf import settings
from products.models import Product
from django.utils import timezone
from django.forms.models import model_to_dict

#from accounts.forms import UserLoginForm, GuestForm
#from accounts.models import GuestEmail

#from addresses.forms import AddressCheckoutForm
#from addresses.models import Address

#from billing.models import BillingProfile
#from orders.models import Order
#from products.models import Product
from carts.models import Cart

@login_required()
def checkout(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    order_obj,created=Order.objects.new_or_get(request)
    order_form=OrderForm(initial=model_to_dict(order_obj))
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart_obj, new_obj = Cart.objects.new_or_get(request)
            total = 0
            cart = model_to_dict(cart_obj)
            '''
            for product in cart.products.all:
                quantity=1
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                    )
                order_line_item.save()
            '''
    else:
        payment_form = MakePaymentForm()
    return render(request, "checkout.html", {'order_form': order_form,'cart_obj':cart_obj})