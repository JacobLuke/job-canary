from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.contrib import admin
admin.autodiscover()
import user.urls
from django.conf.urls.static import static
import employer.urls
import jobs.urls
import owner.urls

def quick_render(file):
    return lambda response: render(response, file)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'job_canary.views.home', name='home'),
    # url(r'^job_canary/', include('job_canary.foo.urls')),
        url(r'^$', quick_render("index.html")),
        url(r'^index', quick_render("index.html")),
        url(r'^register', quick_render("register.html")),
		url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^user/', include(user.urls)),
		url(r'^admin/', include(admin.site.urls)),
        url(r'^employer/', include(employer.urls)),
        url(r'^jobs/', include(jobs.urls)),
        url(r'^owner/', include(owner.urls)),
)
