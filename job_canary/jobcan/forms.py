from django import forms

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
    
class JobForm(forms.Form):
    description = forms.CharField(max_length=5000)
    title = forms.CharField(max_length=5000)
    

