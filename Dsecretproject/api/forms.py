from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):
    nickname = forms.CharField(
        label="Nickname",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your nickname'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )
    class Meta:
        model = User
        fields = ['username', 'nickname', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }
        labels = {
            'nickname': 'Nickname',
            'password2': 'Confirm Password',
        }
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label = "Username",
        widget = forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
