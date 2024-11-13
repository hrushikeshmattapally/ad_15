# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import JournalEntry

# Sign Up form (User Registration)
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login form (Authentication)
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

#journal entry
class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content']

from .models import Note, Label

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'reminder_date']