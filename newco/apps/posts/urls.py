from django.conf.urls import url
from .views import PostListView, NewPost

urlpatterns = [
    url(r'add/$', NewPost.as_view(), name='post_create'),
    url(r'list/$', PostListView.as_view(), name='list_posts'),
]
