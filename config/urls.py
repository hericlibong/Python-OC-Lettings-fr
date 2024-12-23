from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found, server_error


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oc_lettings_site.urls', namespace='oc_lettings_site')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('404/', lambda request: page_not_found(request, exception=None)),  # Test 404 page
    path('500/', lambda request: server_error(request)),  # Test 500 page
]
