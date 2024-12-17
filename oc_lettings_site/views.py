from django.shortcuts import render


def index(request):
    return render(request, 'oc_lettings_site/index.html')

# def cause_error(request):
#     """ This view raises an exception to test the error page. """
#     raise Exception('This is a test error')
