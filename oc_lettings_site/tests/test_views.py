from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
import logging

logger = logging.getLogger("oc_lettings_site.views")


class OcLettingsSiteViewsTest(TestCase):
    def test_index_view(self):
        """
        Teste que la vue 'index' retourne un statut 200 et utilise le bon template.
        """
        response = self.client.get(reverse('oc_lettings_site:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')
        self.assertContains(response, 'Welcome to Holiday Homes')

    def test_index_view_logs_error(self):
        """
        Test que la vue index journalise une erreur et lève une exception en cas d'erreur.
        """
        # Simule une exception dans la fonction `render`
        with patch("oc_lettings_site.views.render", side_effect=Exception("Test exception")):
            with self.assertLogs("oc_lettings_site.views", level="ERROR") as log:
                with self.assertRaises(Exception):  # Vérifie que l'exception est levée
                    self.client.get(reverse("oc_lettings_site:index"))

                # Vérifie que le message attendu est journalisé
                self.assertTrue(
                    any("Error in oc_lettings_site index view: Test exception" in message for message in log.output),
                    f"Logs enregistrés : {log.output}",
                )
