from django.apps import apps
from lettings.apps import LettingsConfig


def test_lettings_app():
    """
    Test that the LettingsConfig is correctly registered in Django.
    """
    assert LettingsConfig.name == 'lettings'
    assert apps.get_app_config('lettings').name == 'lettings'
