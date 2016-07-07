from django.conf.urls import url, include

from newco.apps.apiv1.views import UserListView, PostListView, UserProfileListView

urlpatterns = [
    url(r'users', UserListView.as_view()),
    url(r'posts', PostListView.as_view()),
    url(r'profiles', UserProfileListView.as_view()),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
