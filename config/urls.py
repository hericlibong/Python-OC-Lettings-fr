from django.contrib import admin
from django.urls import path, include

# from profiles.views import profiles_index, profile
# from lettings.views import lettings_index, letting
from oc_lettings_site.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    # path('lettings/<int:letting_id>/', letting, name='letting'),
    # path('lettings/', lettings_index, name='lettings_index'),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    # path('profiles/', profiles_index, name='profiles_index'),
    # path('profiles/<str:username>/', profile, name='profile'),
]
