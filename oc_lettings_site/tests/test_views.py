from django.test import TestCase
from django.urls import reverse

class OcLettingsSiteViewsTest(TestCase):
    def test_index_view(self):
        """
        Teste que la vue 'index' retourne un statut 200 et utilise le bon template
        """
        response = self.client.get(reverse('oc_lettings_site:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')
        self.assertContains(response, 'Welcome to Holiday Homes') # Vérifie que le message de la page d'accueil est affiché
