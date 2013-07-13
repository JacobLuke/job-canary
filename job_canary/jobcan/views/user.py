
from django.shortcuts import get_object_or_404,get_list_or_404, render
from jobcan.models import Candidate, Application

def getUser(request):
    return get_object_or_404(Candidate, pk=request.GET['id'])

def profile(request):
    context = {'user' : getUser(request)}
    return render(request, 'user/profile.html', context)

def jobs(request):
    context = {}
    user = getUser(request)
    context['user'] = user
    try:
        apps = get_list_or_404(Application, candidate=user)
        context['applications'] = apps
    except:pass
    print jobs
    return render(request, "user/jobs.html", context)

def upload(request):
    context = {'user' : getUser(request)}
    return render(request, 'user/upload.html', context)