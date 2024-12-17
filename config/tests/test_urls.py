from django.test import SimpleTestCase
from django.urls import reverse, resolve


class ConfigUrlsTest(SimpleTestCase):
    def test_profiles_namespace(self):
        """
        Vérifie que l'application 'profiles' a un espace de nom 'profiles'
        """
        url = reverse('profiles:index')
        self.assertIsNotNone(resolve(url))

    def test_lettings_namespace(self):
        """
        Vérifie que l'application 'lettings' a un espace de nom 'lettings'
        """
        url = reverse('lettings:index')
        self.assertIsNotNone(resolve(url))

    def test_homepage(self):
        """
        Vérifie le namespace de la page d'accueil
        """
        url = reverse('oc_lettings_site:index')
        self.assertIsNotNone(resolve(url))
