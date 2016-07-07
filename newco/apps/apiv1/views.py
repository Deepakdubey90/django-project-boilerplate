""" Views for Api"""
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from newco.apps.clients.models import Client
from newco.apps.posts.models import Posts
from newco.apps.profiles.models import UserProfile


class UserListView(APIView):
    def get(self, request, format=None):
        usernames = [{'name': client.name} for client in Client.objects.all()]
        return Response(usernames)


class PostListView(APIView):
    def get(self, request, format=None):
        titles = [{'title': post.title} for post in Posts.objects.all()]
        return Response(titles)


class UserProfileListView(APIView):
    def get(self, request, format=None):
        usernames = [{'profile_user_name': userprofile.profile_user.name} for userprofile in UserProfile.objects.all()]
        return Response(usernames)
