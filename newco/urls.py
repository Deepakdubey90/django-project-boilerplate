from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newco.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^client/', include('newco.apps.clients.urls', namespace='clients')),
    url(r'', include('newco.apps.dashboard.urls', namespace='dashboard')),

)
