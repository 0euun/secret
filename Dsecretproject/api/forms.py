from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=''
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text=''
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': '',
        }