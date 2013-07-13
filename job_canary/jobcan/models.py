from django.db import models

def content_file_name(instance, filename):
    return '/'.join(['content', instance.name, filename])

class Company(models.Model):
  description = models.CharField(max_length=1000)
  name = models.CharField(max_length=30)

class Cycle(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=1000)
  start_date = models.DateTimeField('start_date')
  end_date = models.DateTimeField('end_date')
  
class Job(models.Model):
  cycle = models.ForeignKey(Cycle, blank=True, null=True)
  company = models.ForeignKey(Company)
  title = models.CharField(max_length=300)
  description = models.CharField(max_length=1000)

class Candidate(models.Model):
  description = models.CharField(max_length=1000)
  name = models.CharField(max_length=30)
  resume  = models.FileField(upload_to=content_file_name, blank=True, null=True)
  
class Application(models.Model):
  description = models.CharField(max_length=1000)
  name = models.CharField(max_length=30)
  resume  = models.FileField(upload_to=content_file_name)
  job = models.ForeignKey(Job)
  candidate = models.ForeignKey(Candidate)