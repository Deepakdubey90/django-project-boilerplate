from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import (adduser, deleteuser)

urlpatterns = patterns('',
    url(r'^add/$', adduser, name='add_user'),
    url(r'^delete/$', deleteuser, name='delete_user'),
)