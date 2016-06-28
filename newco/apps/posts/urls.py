from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy as reverse
from newco.apps import posts
from .views import PostListView, NewPost

urlpatterns = [
    url(r'add/$', NewPost.as_view(), name='post_create'),
    url(r'list/$', PostListView.as_view(), name='list_posts'),
]
