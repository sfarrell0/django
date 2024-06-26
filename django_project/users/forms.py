from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AmongUsForm(UserCreationForm):
    email = forms.EmailField() #default: required=True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
