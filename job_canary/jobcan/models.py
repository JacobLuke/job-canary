from django.db import models

class Cycle(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=1000)
  start_date = models.DateTimeField('start_date')
  end_date = models.DateTimeField('end_date')
  
class Job(models.Model):
  cycle = models.ForeignKey(Cycle)
  company = models.ForeignKey(Company)
  title = models.CharField(max_length=300)
  description = models.CharField(max_length=1000)

class Company(models.Model):
  description = models.CharField(max_length=1000)
  name = models.CharField(max_length=30)

class Candidate(models.Model):
  description = models.CharField(max_length=1000)
  name = models.CharField(max_length=30)
  resume  = forms.FileField()
  
class Application(models.Model):
  description = models.CharField(max_length=1000)
  name = models.CharField(max_length=30)
  resume  = forms.FileField()
  job = models.ForeignKey(Job)
  candidate = models.ForeignKey(Candidate)