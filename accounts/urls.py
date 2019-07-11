from django.conf.urls import url, include
from .views import register, profile, logout, user_login

urlpatterns = [
    url('register/',register, name='register'),
    url('profile/',profile, name='profile'),
    url('logout/',logout, name='logout'),
    url('login/',user_login, name='login'),
]
