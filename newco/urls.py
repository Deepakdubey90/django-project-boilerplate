from django.conf.urls import patterns, include, urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
from djang.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^client/', include('newco.apps.clients.urls', namespace='clients')),
    url(r'', include('newco.apps.dashboard.urls', namespace='dashboard')),
    url(r'^posts/', include('newco.apps.posts.urls', namespace='posts')),
    url(r'^profiles/', include('newco.apps.profiles.urls', namespace='profiles')),
    url(r'^apiv1/', include('newco.apps.apiv1.urls', namespace='apiv1')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
