
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('index/', views.index, name='index'),  # Protected index page
    path('sign-in/', LogoutView.as_view(next_page='sign_in'), name='logout'),
    path('journal/', views.journal_list, name='journal_list'),
    path('new/', views.journal_create, name='journal_create'),
    path('notes/', views.notes_list, name='note_list'),
    path('delete/<int:pk>/', views.journal_delete, name='journal_delete'),
    path('create/', views.note_create, name='note_create'),
    path('update/<int:pk>/', views.note_update, name='note_update'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
    path('note/', views.notes_view, name='notes'),
    path('reminders/', views.reminders, name='reminders'),
    path('edit_labels/', views.edit_labels, name='edit_labels'),
    path('archive/', views.archive, name='archive'),
    path('trash/', views.trash, name='trash'),
    path('add_note/', views.add_note, name='add_note'),
    path('note/<int:note_id>/', views.get_note_details, name='get_note_details'),
]