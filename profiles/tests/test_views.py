from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


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
