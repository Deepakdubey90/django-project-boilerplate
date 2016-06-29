from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .views import (ClientListView, NewClient)

urlpatterns = [
    url(r'^add/$', NewClient.as_view(), name='add_user'),
    url(r'^list/$', ClientListView.as_view(), name='list_users'),
]
