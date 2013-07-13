
from django.shortcuts import get_object_or_404,get_list_or_404, render
from jobcan.models import Candidate, Application, Company, Job

def getCompany(request):
    return get_object_or_404(Company, pk=request.GET['id'])

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
