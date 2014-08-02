from django.conf.urls import patterns, include, url
from .forms import CustomAuthenticationForm
from django.core.urlresolvers import reverse_lazy as reverse
from .views import dashboard, login

urlpatterns = patterns('',
    url(r'^$', dashboard, name='home'),
    url('^login/$', login, {'authentication_form': CustomAuthenticationForm }, name='login'),
)


