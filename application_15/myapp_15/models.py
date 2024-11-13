from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Label(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    pinned = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_trashed = models.BooleanField(default=False)
    reminder_date = models.DateTimeField(null=True, blank=True)
    labels = models.ManyToManyField(Label, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title