from django.conf.urls import url
from .views import do_search

urlpatterns = [
    url(r'^search/$', do_search, name='search')
]