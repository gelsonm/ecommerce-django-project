from django.conf.urls import url, include
from .views import ProductListView, product_list_view, ProductDetailView, product_detail_view

urlpatterns = [
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products-fbv/$', product_list_view),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    ]
