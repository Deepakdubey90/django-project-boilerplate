from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import (deleteuser, add_user, ClientListView)

urlpatterns = patterns('',
    url(r'^add/$', add_user, name='add_user'),
    url(r'^list/$', ClientListView.as_view(), name='list_users'),
    url(r'^delete/$', deleteuser, name='delete_user'),
)