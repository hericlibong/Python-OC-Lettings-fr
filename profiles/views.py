import logging
from django.shortcuts import render
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the list of user profiles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'profiles/index.html' template with all profiles.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(f"Error in profiles index view: {e}")
        raise


def profile(request, username):
    """
    Render the details of a specific user profile.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: The rendered 'profiles/profile.html' template with profile details.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        logger.error(f"Error in profiles profile view: {e}")
        raise
