from django.core.urlresolvers import reverse_lazy as reverse
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, CreateView
# Create your views here.
from newco.apps.posts.forms import PostForm
from newco.apps.posts.models import Posts


class PostMixin(object):
    model = Posts
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Posts'})
        return kwargs


class PostFormMixin(PostMixin):
    form_class = PostForm
    template_name = 'posts/templates/post_create.html'


class NewPost(PostFormMixin, CreateView):
    def get_success_url(self):
        return reverse('dashboard:home')


class PostListView(ListView):
    model = Posts
