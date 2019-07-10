from django.conf.urls import url, include
from .views import register, profile, logout, login

urlpatterns = [
    url('register/',register, name='register'),
    url('profile/',profile, name='profile'),
    url('logout/',logout, name='logout'),
    url('login/',login, name='login'),
]
