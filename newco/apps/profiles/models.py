from django.db import models


class UserProfile(models.Model):
    """
    User Profile Model
    """
    profile_user = models.ForeignKey('clients.Client',
                                     verbose_name='Profile User',
                                     related_name='profile_user')
    picture = models.FileField(upload_to='media/%Y/%m/%d',
                               null=True, blank=True)
    info = models.TextField(max_length=500, verbose_name='Profile Information')
    status = models.CharField(max_length=100, verbose_name='status')
