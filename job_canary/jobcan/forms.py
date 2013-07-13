from django import forms

class RegisterForm(forms.Form):
    email_addr = forms.CharField(max_length=5000)
    description = forms.CharField(max_length=5000)
    name = forms.CharField(max_length=5000)
    resume = forms.FileField()
    
class EmployerRegisterForm(forms.Form):
    email_addr = forms.CharField(max_length=5000)
    description = forms.CharField(max_length=5000)
    name = forms.CharField(max_length=5000)

class ApplicationForm(forms.Form):
    description = forms.CharField(max_length=5000)
    
class JobForm(forms.Form):
    description = forms.CharField(max_length=5000)
    title = forms.CharField(max_length=5000)
    

