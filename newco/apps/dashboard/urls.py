from django.conf.urls import patterns, include, url
from .forms import CustomAuthenticationForm
from .views import home
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^$', home, name='home'),
    url('^login/$', login, name='login'),
    url('^logout/$', logout_then_login, name='logout'),
]


