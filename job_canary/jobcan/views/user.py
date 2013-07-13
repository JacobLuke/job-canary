
from django.shortcuts import get_object_or_404,get_list_or_404, render
from jobcan.models import Candidate, Application

def getUser(request):
    return get_object_or_404(Candidate, pk=request.GET['id'])

def profile(request):
    context = {}
    try:
        context["user"] = getUser(request)
    except:raise
    return render(request, 'user/profile.html', context)

def jobs(request):
    context = {}
    try:
        user = getUser(request)
        context['user'] = user
        jobs = get_list_or_404(Application, candidate=user)
        context['jobs'] = jobs
        print jobs
    except:raise
    return render(request, "user/jobs.html", context)

def upload(request):
    context = {}
    try:
        context['user'] = getUser(request)
    except:raise
    return render(request, 'user/upload.html', context)