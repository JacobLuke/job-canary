from django.conf.urls import patterns, include, url
import jobcan.views as views
print(dir(views))
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'job_canary.views.home', name='home'),
                       # url(r'^job_canary/', include('job_canary.foo.urls')),
                       
                       url(r'^profile', views.user.profile, name="profile"))
