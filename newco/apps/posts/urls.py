from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy as reverse
from .views import PostFormView, add_post

urlpatterns = patterns('',
    url(r'create/$', add_post, name='post_create'),
)
