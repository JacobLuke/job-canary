from django import forms
import jobcan.models

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=5000)
    email_addr = forms.CharField(max_length=5000)
    resume = forms.FileField()
    description = forms.CharField(max_length=5000)

class OwnerRegisterForm(forms.Form):
    name = forms.CharField(max_length=300)
    email_addr = forms.CharField(max_length=5000)

class EmployerRegisterForm(forms.Form):
    name = forms.CharField(max_length=5000)
    email_addr = forms.CharField(max_length=5000)
    description = forms.CharField(max_length=5000)

class OwnerRegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    email_address = forms.CharField(max_length=5000)

class ApplicationForm(forms.Form):
    description = forms.CharField(max_length=5000)
    def __init__ (self, *args, **kw):
        super(ApplicationForm, self).__init__(*args, **kw)
        self.fields['job'] = forms.ModelChoiceField(queryset=jobcan.models.Job.objects)

class JobForm(forms.Form):
    title = forms.CharField(max_length=5000)
    description = forms.CharField(max_length=5000)
    def __init__ (self, *a, **k):
        super(JobForm, self).__init__(*a,**k)
        self.fields['cycle'] = forms.ModelChoiceField(queryset=jobcan.models.Cycle.objects)

class CycleRegistration(forms.Form):
    name = forms.CharField(max_length=500)
    description=forms.CharField(max_length=500)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    candidates = forms.ModelMultipleChoiceField(queryset=jobcan.models.Candidate.objects)