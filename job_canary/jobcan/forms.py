from django import forms

class RegisterForm(forms.Form):
    email_addr = forms.CharField(max_length=5000)
    description = forms.CharField(max_length=5000)
    name = forms.CharField(max_length=5000)
    resume = forms.FileField()