from django.db import models

def content_file_name(instance, filename):
    return '/'.join(['content', instance.name, filename])

class Company(models.Model):
  description = models.CharField(max_length=1000)
  name = models.CharField(max_length=30)
  email_addr = models.CharField(max_length=100)
  def __str__ (self):
    return self.name

class Cycle(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=1000)
  start_date = models.DateTimeField('start_date')
  end_date = models.DateTimeField('end_date')
  def __str__(self):
    return "{0} [{1} - {2}]".format(self.name, self.start_date, self.end_date)
  
class Job(models.Model):
  cycle = models.ForeignKey(Cycle, blank=True, null=True)
  company = models.ForeignKey(Company)
  title = models.CharField(max_length=300)
  description = models.CharField(max_length=1000)
  def __str__ (self):
    return "\"{0}\" at {1} ({2})".format(self.title, self.company, self.cycle)

class Candidate(models.Model):
  description = models.CharField(max_length=1000)
  name = models.CharField(max_length=30)
  resume  = models.FileField(upload_to=content_file_name, blank=True, null=True)
  linkedindata = models.CharField(max_length=5000)
  company = models.ForeignKey(Company, blank=True, null=True)
  email_addr = models.CharField(max_length=100)
  def __str__(self):
        return self.name

class Application(models.Model):
  description = models.CharField(max_length=1000)
  name = models.CharField(max_length=30)
  resume  = models.FileField(upload_to=content_file_name)
  job = models.ForeignKey(Job)
  candidate = models.ForeignKey(Candidate)
  status = models.CharField(max_length=20)
  def __str__(self):
     return "{1} - {0} ({2})".format(self.name, self.candidate, self.status)
