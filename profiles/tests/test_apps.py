from django.apps import apps
from profiles.apps import ProfilesConfig


def test_profiles_app():
    """
    Test that the ProfilesConfig is correctly registered in Django.
    """
    assert ProfilesConfig.name == 'profiles'
    assert apps.get_app_config('profiles').name == 'profiles'
