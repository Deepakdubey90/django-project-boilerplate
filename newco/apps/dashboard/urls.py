from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy as reverse
from .views import dashboard

urlpatterns = patterns('',
    url(r'^$', dashboard, name='home'),
)
