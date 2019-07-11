"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url('', all_products, name='index'),
    #path(r'^$', home_view,name='index'),
    path('', include('home.urls')),
    path('',include('products.urls')),
    path('cart/',include('carts.urls')),
    path('',include('search.urls')),
    path('',include('accounts.urls')),
    path('admin/', admin.site.urls),
]

'''
urlpatterns = [
    #url(r'^$', home_page),
    #url(r'^about/$', about_page),
    #url(r'^contact/$', contact_page),
    #url(r'^login/$', login_page),
    #url(r'^register/$', register_page),
    #url(r'^products/$', ProductListView.as_view()),
    #url(r'^products-fbv/$', product_list_view),
    #url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    #url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    url(r'^admin/', admin.site.urls),
]
'''

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
