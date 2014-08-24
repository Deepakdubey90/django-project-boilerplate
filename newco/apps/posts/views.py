"""views for post"""
from django.core.urlresolvers import reverse_lazy as reverse
from django.views.generic import ListView, CreateView
from newco.apps.posts.forms import PostForm
from newco.apps.posts.models import Posts


class PostMixin(object):
    """post mixin"""
    model = Posts

    def get_context_data(self, **kwargs):
        """setup post in context"""
        kwargs.update({'object_name': 'Posts'})
        return kwargs


class PostFormMixin(PostMixin):
    """Mixins for PostForm"""
    form_class = PostForm
    template_name = 'posts/templates/post_create.html'


class NewPost(PostFormMixin, CreateView):
    """New Post View"""
    def get_success_url(self):
        return reverse('dashboard:home')


class PostListView(ListView):
    """Post List View"""
    model = Posts
