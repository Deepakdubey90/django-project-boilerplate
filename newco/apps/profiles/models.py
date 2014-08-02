from django.db import models

# Create your models here.


def get_upload_path(self, filename):
    return self.filename

class UserProfile(models.Model):
    profile_user = models.ForeignKey('clients.Client', verbose_name='Profile User', related_name='profile_user')
    picture = models.FileField(upload_to='media/%Y/%m/%d')
    info = models.TextField(max_length=500, verbose_name='Profile Information')
    status = models.CharField(max_length=100, verbose_name='status')