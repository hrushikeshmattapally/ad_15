from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from .models import JournalEntry
from .forms import JournalEntryForm
from django.shortcuts import get_object_or_404
from django.urls import reverse

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
    print("Logged-in user:", request.user)
    return render(request, 'index.html')
@login_required
def journal_list(request):
    entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'accounts/journal_list.html', {'entries': entries})
@login_required
def journal_create(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            # Ensure the user is assigned to the journal entry
            journal_entry = form.save(commit=False)  # Don't save yet, to add the user
            journal_entry.user = request.user  # Set the logged-in user as the owner
            journal_entry.save()  # Now save the journal entry
            return redirect('journal_list')
    else:
        form = JournalEntryForm()
    return render(request, 'accounts/journal_create.html', {'form': form})

def journal_delete(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect(reverse('journal_list'))
    return render(request, 'accounts/journal_delete_confirm.html', {'entry': entry})


from django.shortcuts import render
@login_required
def notes_list(request):
    # Add your notes retrieval logic here
    return render(request, 'notes_list.html')
