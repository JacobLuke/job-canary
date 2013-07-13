from django.db import models
DB model
Cycle (id, name, description, startdate, enddate)
Job (id, company_id, description, title, cycle_id)
Company(id, description, name)
Candidate(id, description, name, resume(PDF))

class Cycle(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=1000)
  start_date = models.DateTimeField('start_date')
  end_date = models.DateTimeField('end_date')
  
class Job(models.Model):
    cycle = models.ForeignKey(Cycle)
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=300)
    