from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'job_canary.views.home', name='home'),
    # url(r'^job_canary/', include('job_canary.foo.urls')),

		url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

		url(r'^admin/', include(admin.site.urls)),
)
