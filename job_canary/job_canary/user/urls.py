import jobcan.views as views
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url('^profile', views.user.profile, name="profile"),
                       url('^register', views.user.register, name="register"),
                       url('^application', views.user.application, name="application"),
                       url('^jobs', views.user.jobs, name="Jobs"),
                       url('^upload', views.user.upload, name="Upload file"),
                       url('^profile', views.user.profile, name="profile")
                       )
