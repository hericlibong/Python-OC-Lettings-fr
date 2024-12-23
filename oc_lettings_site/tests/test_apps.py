from django.apps import apps
from oc_lettings_site.apps import OCLettingsSiteConfig


def test_oc_lettings_site_app():
    """
    Test that the OCLettingsSiteConfig is correctly registered in Django.
    """
    assert OCLettingsSiteConfig.name == 'oc_lettings_site'
    assert apps.get_app_config('oc_lettings_site').name == 'oc_lettings_site'
