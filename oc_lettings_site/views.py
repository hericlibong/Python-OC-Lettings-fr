from django.shortcuts import render


def index(request):
    """
    Render the homepage of the application.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'oc_lettings_site/index.html' template.
    """
    return render(request, 'oc_lettings_site/index.html')

# def cause_error(request):
#     """ This view raises an exception to test the error page. """
#     raise Exception('This is a test error')
