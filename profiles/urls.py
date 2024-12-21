"""
URL configuration for the profiles application.

This module defines the routes for the profiles application, which include:
- The list of all user profiles.
- The details of a specific user profile.

Namespace:
    'profiles' - Used to avoid conflicts with other applications' URLs.
"""


from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]