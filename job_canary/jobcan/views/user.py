from django.shortcuts import get_object_or_404, render, render_to_response
from jobcan.models import Candidate
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

<<<<<<< HEAD
from jobcan.forms import RegisterForm
import oauth2 as oauth
import urlparse 
from jobcan.models import Candidate
=======
from django.shortcuts import get_object_or_404,get_list_or_404, render
from jobcan.models import Candidate, Application

def getUser(request):
    return get_object_or_404(Candidate, pk=request.GET['id'])
>>>>>>> a93e6df89e0dbeaa980d5367484e4d702acfec9b

consumer_key           = "CONSUMER_KEY"
consumer_secret        = "CONSUMER_SECRET"
consumer = oauth.Consumer(consumer_key, consumer_secret)

def profile(request):
    context = {'user' : getUser(request)}
    return render(request, 'user/profile.html', context)

def jobs(request):
    context = {}
    user = getUser(request)
    context['user'] = user
    try:
<<<<<<< HEAD
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
=======
        apps = get_list_or_404(Application, candidate=user)
        context['applications'] = apps
    except:pass
    print jobs
    return render(request, "user/jobs.html", context)

def upload(request):
    context = {'user' : getUser(request)}
    return render(request, 'user/upload.html', context)
>>>>>>> a93e6df89e0dbeaa980d5367484e4d702acfec9b
