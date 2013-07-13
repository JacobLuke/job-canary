
from django.shortcuts import get_object_or_404, render
from jobcan.models import Candidate

def profile(request):
    context = {}
    try:
        id = request.GET['id']
        user = get_object_or_404(Candidate, pk=id)
        context["user"] = user
    except:raise
    return render(request, '../../templates/user/profile.html', context)