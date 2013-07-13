from django.conf.urls import patterns, url, include
import jobcan.views as views

urlpatterns = patterns("",
                       url(r'^applications', views.employer.applications),
                       url(r'^jobs', views.employer.jobs),
                       url(r'^profile', views.employer.profile))
