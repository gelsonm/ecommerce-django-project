from django.db import models
from products.models import Product
from django.conf import settings
User = settings.AUTH_USER_MODEL

class OrderManager(models.Manager):
    def new_or_get(self, request):
        created = False
        qs = self.get_queryset().filter(user=request.user)
        if qs.count() >= 1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(user=request.user)
            created = True
        return obj, created


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    pincode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    date = models.DateField(null=True)

    objects = OrderManager()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False,on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.title, self.product.price)