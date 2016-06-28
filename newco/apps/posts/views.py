"""views for post"""
from django.core.urlresolvers import reverse_lazy as reverse
from django.views.generic import ListView, CreateView, FormView
from newco.apps.posts.forms import PostForm
from newco.apps.posts.models import Posts

class NewPost(FormView):
    form_class = PostForm
    template_name = 'posts/templates/post_create.html'

    """New Post View"""
    def get_success_url(self):
        return reverse('dashboard:home')


class PostListView(ListView):
    """Post List View"""
    model = Posts
