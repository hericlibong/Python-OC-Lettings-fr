"""
URL configuration for the lettings application.

This file defines the routes for the lettings application, which include:
- The list of all lettings.
- The details of a specific letting.

Namespace:
    'lettings' - Used to avoid conflicts with other applications' URLs.
"""

from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
