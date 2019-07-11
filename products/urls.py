from django.conf.urls import url, include
from .views import all_products,product_detail

urlpatterns = [
    url(r'^products/$', all_products,name='shop'),
    url(r'^product/(?P<id>\d+)/$', product_detail,name='productdetail'),

]
