from django.conf.urls import url
from .views import ProfileList, NewProfile

urlpatterns = [
    url(r'add/$', NewProfile.as_view(), name='profile_create'),
    url(r'list/$', ProfileList.as_view(), name='list_profiles'),
]
