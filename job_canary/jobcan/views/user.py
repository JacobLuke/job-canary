from django.shortcuts import get_object_or_404, render, render_to_response, get_list_or_404
from jobcan.models import Candidate, Application, Job
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from jobcan.forms import RegisterForm, ApplicationForm
import urlparse 

def getUser(request):
    return get_object_or_404(Candidate, pk=request.GET['id'])

def getJob(request):
	return get_object_or_404(Job, pk=request.GET['jobid'])

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

def application(request):
	user = getUser(request)
	job = getJob(request)
	context = {}
	if request.method == 'POST':
		form = ApplicationForm(request.POST)
		if form.is_valid():
			application = Application(
				description=request.POST['description'],
				name=request.POST['name'],
				resume=user.resume,
				candidate=user,
				job=job,
			)
			application.save()
			return HttpResponseRedirect('/user/profile?id=%d' % user.id)
	else:
		form = RegisterForm()
	context['form'] = form
	context['user'] = user
	context['job'] = job
	return render(request, 'user/profile.html', context)

def upload(request):
    context = {'user' : getUser(request)}
    return render(request, 'user/upload.html', context)
