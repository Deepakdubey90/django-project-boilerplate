from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy as reverse
from newco.apps import posts
from .views import PostListView, add_post

urlpatterns = patterns('',
    url(r'add/$', add_post, name='post_create'),
    url(r'list/$', PostListView.as_view(), name='list posts'),
)
