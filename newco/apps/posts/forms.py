from django.forms import ModelForm
from newco.apps.posts.models import Posts


class PostForm(ModelForm):
    """
    Post Form
    """
    class Meta:
        model = Posts
        fields = ('title', 'content', 'tags', 'user',)
