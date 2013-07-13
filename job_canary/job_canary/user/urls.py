import jobcan.views as views
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url('^profile', views.user.profile, name="profile"),
<<<<<<< HEAD
                       url('^register', views.user.register, name="register")
=======
                       url('^jobs', views.user.jobs, name="Jobs"),
                       url('^upload', views.user.upload, name="Upload file")
>>>>>>> a93e6df89e0dbeaa980d5367484e4d702acfec9b
                       )