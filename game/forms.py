from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
