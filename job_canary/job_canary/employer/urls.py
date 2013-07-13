from django.conf.urls import patterns, url, include
import jobcan.views as views

urlpatterns = patterns("",
                       url(r'^application', views.employers.applications),
                       url(r'^jobs', views.employers.jobs),
                       url(r'^profile', views.employers.profile))
