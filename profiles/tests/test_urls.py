from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import index, profile

class ProfilesUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        """
        Teste que l'URL de 'index' appelle la bonne vue 
        """
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, index)

    def test_profile_url_resolves(self):
        """
        Teste que l'URL de 'profile' appelle la bonne vue avec un paramètre dynamique
        """
        url = reverse('profiles:profile', args=['testuser'])
        self.assertEqual(resolve(url).func, profile)
