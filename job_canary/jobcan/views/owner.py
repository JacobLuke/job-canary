from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from jobcan.models import Owner
from jobcan.forms import OwnerRegisterForm, CycleRegistration

def getOwner(request):
    return get_object_or_404(Owner, pk=request.GET['id'])

def profile(request):
    context = {'owner': getOwner(request)}
    return render(request, 'owner/profile.html', context)


def register(request):
	print request
	context = {}
	if request.method == 'POST':
		form = OwnerRegisterForm(request.POST, request.FILES)
		print form
		if form.is_valid():
			owner = Owner(name=request.POST['name'],
                          email_address=request.POST['email_address']
                          )
			owner.save()
			return HttpResponseRedirect('/owner/profile?id=%d' % owner.id)
	else:
		form = OwnerRegisterForm()
	context['form'] = form
	return render(request, 'owner/register.html', context)

def create(request):
	print request
	context = {}
	if request.method == 'POST':
		form = CycleRegistration(request.POST, request.FILES)
		print form
		if form.is_valid():
			owner = Owner(name=request.POST['name'],
                          email_address=request.POST['email_address']
                          )
			owner.save()
			return HttpResponseRedirect('/owner/profile?id=%d' % owner.id)
	else:
		form = CycleRegistration()
	context['form'] = form
	return render(request, 'owner/create.html', context)


def cycles(request):
    '''
    shows all cycles (and lets the user add members to a cycle)
    '''
    pass