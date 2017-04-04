from django.conf.urls import url, include
from rest_framework import routers
from newco.apps.apiv1 import views

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
