from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from api. forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})