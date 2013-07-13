import jobcan.views as views
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url('^profile', views.user.profile, name="profile")
                       )