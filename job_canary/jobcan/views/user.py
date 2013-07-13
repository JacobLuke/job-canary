
from django.shortcuts import get_object_or_404, render
from jobcan.models import Candidate
import os

def profile(request):
    context = {}
    try:
        id = request.GET['id']
        user = get_object_or_404(Candidate, pk=id)
        context["user"] = user
    except:raise
    open(os.environ['JOBCANARY_ROOT'] + '/templates/user/profile.html')
    return render(request,'user/profile.html', context)