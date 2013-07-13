
from django.shortcuts import get_object_or_404,get_list_or_404, render
from jobcan.models import Candidate, Application

def profile(request):
    context = {}
    try:
        id = request.GET['id']
        user = get_object_or_404(Candidate, pk=id)
        context["user"] = user
    except:raise
    return render(request, 'user/profile.html', context)

def jobs(request):
    context = {}
    try:
        id = request.GET['id']
        user = get_object_or_404(Candidate, pk=id)
        context['user'] = user
        jobs = get_list_or_404(Application, candidate=user)
        context['jobs'] = jobs
        print jobs
    except:raise
    return render(request, "user/jobs.html", context)