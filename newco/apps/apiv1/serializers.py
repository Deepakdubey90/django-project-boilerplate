from rest_framework import serializers
from newco.apps.posts.models import Posts
from newco.apps.clients.models import Client
from newco.apps.profiles.models import UserProfile


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'email', 'address')


class PostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('title', 'content', 'tags', 'user',)


class ProfileSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('profile_user', 'picture', 'info', 'status')