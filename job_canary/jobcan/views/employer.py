
from django.shortcuts import get_object_or_404,get_list_or_404, render
from jobcan.models import Candidate, Application, Company, Job, Company, Cycle
from django.http import HttpResponseRedirect

from jobcan.forms import EmployerRegisterForm, ApplicationForm

def getCompany(request):
    return get_object_or_404(Company, pk=request.GET['id'])
    
def getCycle(request):
	return get_object_or_404(Cycle, pk=request.GET['cycleid'])

def profile(request):
    context = {'company' : getCompany(request)}
    return render(request, 'employer/profile.html', context)

def jobs(request):
    context = {}
    company = getCompany(request)
    context['company'] = company
    try:
        jobs = get_list_or_404(Job, company=company)
        context['jobs'] = jobs
    except:pass
    print jobs
    return render(request, "employer/jobs.html", context)

def applications(request):
    context = {}
    company = getCompany(request)
    context['company'] = company
    try:
	jobs = get_list_or_404(Job, company=company)
        applications = get_list_or_404(Application, job__in=jobs)
        context['applications'] = applications
    except:pass
    print applications
    return render(request, "employer/applications.html", context)

def jobcreation(request):
	user = getCompany(request)
	cycle = getCycle(request)
	context = {}
	if request.method == 'POST':
		form = JobForm(request.POST)
		if form.is_valid():
			job = Job(
				description=request.POST['description'],
				title=request.POST['title'],
			)
			job.save()
			return HttpResponseRedirect('/employer/profile?id=%d' % user.id)
	else:
		form = JobForm()
	context['form'] = form
	context['user'] = user
	context['cycle'] = cycle
	return render(request, 'employer/jobcreation.html', context)    

def register(request):
	print request
	context = {}
	if request.method == 'POST':
		form = EmployerRegisterForm(request.POST, request.FILES)
		print form
		if form.is_valid():
			employer = Company(description=request.POST['description'],
                                name=request.POST['name'],
                                email_addr=request.POST['email_addr']
                                  )
			employer.save()
			return HttpResponseRedirect('/employer/profile?id=%d' % employer.id)
	else:
		form = EmployerRegisterForm()
	context['form'] = form
	return render(request, 'employer/register.html', context)