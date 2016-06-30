from django.db import models


class Posts(models.Model):
    """
    Post Model
    """
    title = models.CharField(max_length=150, verbose_name='Post title')
    content = models.TextField(max_length='500', verbose_name='Post Content')
    tags = models.CharField(max_length=90, null=True, blank=True,
                            verbose_name='tags')
    user = models.ForeignKey('clients.Client', related_name='user',)
    time = models.DateTimeField(auto_now_add=True)
