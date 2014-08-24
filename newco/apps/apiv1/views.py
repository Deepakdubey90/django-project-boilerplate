""" Views for Api"""
from rest_framework import viewsets

# Create your views here.
from newco.apps.clients.models import Client
from newco.apps.apiv1.serializers import (UserSerializers, PostSerializers,
                                          ProfileSerializers)
from newco.apps.posts.models import Posts
from newco.apps.profiles.models import UserProfile


class UserViewSet(viewsets.ModelViewSet):
    """User View Set"""
    def __init__(self):
        pass

    queryset = Client.objects.all()
    serializer_class = UserSerializers


class ProfileViewSet(viewsets.ModelViewSet):
    """ Profile View Set"""
    def __init__(self):
        pass

    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializers


class PostViewSet(viewsets.ModelViewSet):
    """ Post View Set"""
    def __init__(self):
        pass
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
