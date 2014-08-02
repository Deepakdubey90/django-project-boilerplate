from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy as reverse
from .views import add_profile, ProfileList

urlpatterns = patterns('',
    url(r'add/$', add_profile, name='profile_create'),
    url(r'list/$', ProfileList.as_view(), name='list_profile'),
)