from django.conf.urls import url
from .views import (ClientListView, NewClient)

urlpatterns = [
    url(r'^add/$', NewClient.as_view(), name='add_user'),
    url(r'^list/$', ClientListView.as_view(), name='list_users'),
]
