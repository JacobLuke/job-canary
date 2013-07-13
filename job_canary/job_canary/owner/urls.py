
import jobcan.views as views
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url('^profile', views.owner.profile),
                       url('^register', views.owner.register),
                       url('^create', views.owner.create),
                       url('^cycles', views.owner.cycles)
                      )