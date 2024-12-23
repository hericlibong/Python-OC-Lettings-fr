import logging
from django.shortcuts import render
from .models import Letting

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    """
    Render the list of lettings.

    Args:
        request (HttpRequest): The HTTP request object.e

    Returns:
        HttpResponse: The rendered 'lettings/index.html' template with all lettings.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(f"Error in lettings index view: {e}")
        raise


def letting(request, letting_id):
    """
    Render the details of a specific letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: The rendered 'lettings/letting.html' template with letting details.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        logger.error(f"Error in lettings letting view: {e}")
        raise
