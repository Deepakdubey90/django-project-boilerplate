from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=150, verbose_name='Post title')
    content = models.TextField(max_length='500', verbose_name='Post Content')
    tags = models.CharField(max_length=90, null=True, blank=True, verbose_name='tags')
    user = models.ForeignKey('clients.Client', related_name='user',)
