from django import forms
from django_extensions.tests.testapp.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags', 'user')
