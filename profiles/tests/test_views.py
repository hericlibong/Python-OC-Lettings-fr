from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from unittest.mock import patch
import logging


logger = logging.getLogger('profiles.views')


class ProfilesViewsTest(TestCase):
    def setUp(self):
        # Créer des données de test pour les vues
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        Profile.objects.create(user=self.user, favorite_city='Alençon')

    def test_index_view(self):
        """
        Teste que la vue 'index retourne un statut 200 et utilise le bon template
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, 'testuser')  # Vérifie que le nom d'utilisateur est affiché

    def test_profile_view(self):
        """
        Teste que la vue 'profile' retourne un statut 200 et utilise le bon template
        """
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'testuser')   # Vérifie que le nom utilisateur est affiché
        self.assertContains(response, 'Alençon')    # Vérifie que la ville favorite est affichée

    def test_index_view_logs_error(self):
        """
        Test that the index view logs an error and raises an exception when an error occurs.
        """
        with patch('profiles.models.Profile.objects.all', side_effect=Exception("Test exception")):
            with self.assertLogs(logger, level='ERROR') as log:
                with self.assertRaises(Exception):  # Vérifie que l'exception est levée
                    self.client.get(reverse('profiles:index'))
                # Vérifie que le log contient le message attendu
                self.assertTrue(
                    any("Error in profiles index view: Test exception" in message
                        for message in log.output),
                    f"Actual logs: {log.output}"
                )

    def test_profile_view_logs_error(self):
        """
        Test que la vue profile journalise une erreur et lève une exception en cas d'erreur.
        """
        # Utiliser un mock pour simuler une exception dans Profile.objects.get
        with patch("profiles.models.Profile.objects.get", side_effect=Exception("Test exception")):
            with self.assertLogs(logger, level="ERROR") as log:
                with self.assertRaises(Exception):  # Vérifie que l'exception est levée
                    self.client.get(reverse("profiles:profile", args=["testuser"]))

                # Vérifie que le message d'erreur attendu est bien journalisé
                self.assertTrue(
                    any("Error in profiles profile view: Test exception" in message
                        for message in log.output),
                    f"Logs enregistrés: {log.output}",
                )
