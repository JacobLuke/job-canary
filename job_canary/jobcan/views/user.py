from django.shortcuts import get_object_or_404, render, render_to_response
from jobcan.models import Candidate
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from jobcan.forms import RegisterForm
import oauth2 as oauth
import urlparse 
from jobcan.models import Candidate

consumer_key           = "CONSUMER_KEY"
consumer_secret        = "CONSUMER_SECRET"
consumer = oauth.Consumer(consumer_key, consumer_secret)

def profile(request):
    context = {}
    try:
        id = request.GET['id']
        user = get_object_or_404(Candidate, pk=id)
        context["user"] = user
    except:raise
    return render(request, 'user/profile.html', context)
    
def register(request):
	print request
	context = {}
	if request.method == 'POST':
		form = RegisterForm(request.POST, request.FILES)
		print form
		if form.is_valid():
			candidate = Candidate(
				description=request.POST['description'],
				name=request.POST['name'],
				resume=request.FILES['resume'],
				email_addr=request.POST['email_addr']
			)
			candidate.save()
			return HttpResponseRedirect('/user/profile?id=%d' % candidate.id)
	else:
		form = RegisterForm()
	context['form'] = form
	return render(request, 'user/register.html', context)