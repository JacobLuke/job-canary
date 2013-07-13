
from djagno.shortcuts import get_object_or_404, render
from job_canary.models import Candidate

def profile(request):
    context = {}
    try:
        id = request.POST['id']
        user = get_object_or_404(Candidate, pk=id)
        context["user"] = user
    except:pass
    return render(request, '../../templates/user/profile.html', context)