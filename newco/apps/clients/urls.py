from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import (deleteuser, add_user)

urlpatterns = patterns('',
    url(r'^add/$', add_user, name='add_user'),
    url(r'^delete/$', deleteuser, name='delete_user'),
)