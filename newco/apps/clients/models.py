from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Username')
    email = models.EmailField(max_length=150, verbose_name='Email')
    address = models.TextField(max_length=200, verbose_name='Address')

    def __unicode__(self):
        return self.name