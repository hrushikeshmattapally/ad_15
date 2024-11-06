from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

# Sign Up View (User Registration)
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirect to index after successful signup
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign_up2.html', {'form': form})

# Login View
def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to index after successful login
            else:
                return redirect('login')  # Redirect to login page if authentication fails
    else:
        form = LoginForm()
    return render(request, 'accounts/sign_in.html', {'form': form})

# Index View (Page Only Accessible to Logged-In Users)
@login_required
def index(request):
    return render(request, 'index.html')
