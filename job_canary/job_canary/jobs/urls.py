from django.conf.urls import patterns, url, include
import jobcan.views as views

urlpatterns = patterns("",
                       url(r'^applications', views.jobs.applications)
		      )
