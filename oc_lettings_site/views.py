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
    return render(request, 'oc_lettings_site/index.html')


def test_logging(request):
    """
    Test logging.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'oc_lettings_site/index.html' template.
    """
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    return render(request, 'oc_lettings_site/index.html')


def test_logging_except(request):
    try:
        division_by_zero = 1 / 0
    except ZeroDivisionError as e:
        logger.error("An error occurred: %s", e)
        raise



# def cause_error(request):
#     """ This view raises an exception to test the 500 error page. """
#     raise Exception('This is a test error')
