from django.contrib import admin
from jobcan.models import Cycle, Job, Candidate, Company, Application

admin.site.register(Cycle)
admin.site.register(Job)
admin.site.register(Candidate)
admin.site.register(Company)
admin.site.register(Application)
