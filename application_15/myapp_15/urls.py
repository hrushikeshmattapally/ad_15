
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
    path('notes/', views.notes_list, name='notes_list'),
    path('delete/<int:pk>/', views.journal_delete, name='journal_delete'),
]