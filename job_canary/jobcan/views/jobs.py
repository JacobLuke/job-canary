
from django.shortcuts import get_object_or_404,get_list_or_404, render
from jobcan.models import Candidate, Application, Company, Job

def getJob(request):
    return get_object_or_404(Job, pk=request.GET['id'])

def applications(request):
    context = {}
    job = getJob(request)
    context['job'] = job
    try:
        applications = get_list_or_404(Application, job=job)
        context['applications'] = applications
    except:pass
    print applications
    return render(request, "jobs/application.html", context)
