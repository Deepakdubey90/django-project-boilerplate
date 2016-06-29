"""views for post"""
from django.core.urlresolvers import reverse_lazy as reverse
from django.views.generic import ListView, CreateView

from newco.apps.posts.models import Posts


class NewPost(CreateView):
    model = Posts
    fields = ['title', 'content', 'tags', 'user']
    """New Post View"""
    def get_success_url(self):
        return reverse('dashboard:home')


class PostListView(ListView):
    """Post List View"""
    model = Posts
