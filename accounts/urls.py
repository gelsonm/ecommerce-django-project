from django.conf.urls import url, include
from .views import register, profile, logout, login

urlpatterns = [
    url('register/',register, name='register'),
    url('profile/',profile, name='profile'),
    url('logout/',logout, name='logout'),
    url('login/',login, name='login'),
    #url('password-reset/', include(urls_reset)),
]

'''
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    #url(r'^password-reset/', include(urls_reset)),
]
'''