from django.conf.urls import url, include
from .views import all_products,product_detail

urlpatterns = [
    url(r'^$', all_products,name='index'),
    url(r'^product/(?P<id>\d+)/$', product_detail,name='productdetail'),

]

'''
urlpatterns = [
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products-fbv/$', product_list_view),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    ]
'''