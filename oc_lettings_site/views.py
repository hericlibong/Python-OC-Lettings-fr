from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the homepage of the application.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'oc_lettings_site/index.html' template.
    """
    
    try:
        return render(request, 'oc_lettings_site/index.html')
    except Exception as e:
        logger.error(f"Error in oc_lettings_site index view: {e}")
        raise
    