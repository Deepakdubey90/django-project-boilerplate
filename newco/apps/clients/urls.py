from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .views import (add_user, ClientListView, NewClient)

urlpatterns = patterns('',
    url(r'^add/$', NewClient.as_view(), name='add_user'),
    url(r'^list/$', ClientListView.as_view(), name='list_users'),
    url(r'^delete/$', deleteuser, name='delete_user'),
)
