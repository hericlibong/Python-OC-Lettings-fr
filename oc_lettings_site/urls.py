"""
URL configuration for the oc_lettings_site application.

This module defines the routes for the homepage of the project.

Namespace:
    'oc_lettings_site' - Used to avoid conflicts with other applications' URLs.
"""


from django.urls import path
from . import views

app_name = 'oc_lettings_site'

urlpatterns = [
    path('', views.index, name='index'),
    path('test-logging/', views.test_logging, name='test_logging'),
    # path('test-logging-except/', views.test_logging_except, name='test_logging_except'),
]
