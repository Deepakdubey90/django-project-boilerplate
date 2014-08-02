from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Username')
    email = models.EmailField(max_length=150, verbose_name='Email')
    address = models.TextField(max_length=200, verbose_name='Address')
    slug = models.SlugField(blank=True)
    class Meta:
        verbose_name_plural = 'clients'
    def __unicode__(self):
        return u"%s" % self.name
