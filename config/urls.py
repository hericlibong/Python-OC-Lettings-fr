from django.contrib import admin
# from django.shortcuts import render
from django.urls import path, include
# from django.conf.urls import handler404, handler500
from django.views.defaults import page_not_found, server_error
# from oc_lettings_site.views import cause_error

# def trigger_error(request):
#     division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('oc_lettings_site.urls', namespace='oc_lettings_site')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('404/', lambda request: page_not_found(request, exception=None)),  # Test 404 page
    path('500/', lambda request: server_error(request)),  # Test 500 page
   # path('sentry-debug/', trigger_error),
   # path('error/', cause_error), # Test error page
]

# # Test error page
# def custom_handler404(request, exception):
#     return render(request, '404.html', status=404)

# def custom_handler500(request):
#     return render(request, '500.html', status=500)

# handler404 = custom_handler404
# handler500 = custom_handler500
