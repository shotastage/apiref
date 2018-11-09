from django import forms


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
