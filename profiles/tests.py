from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileTestCase(TestCase):
    def test_profile_str(self):
        user = User.objects.create_user(username='testuser', password='12345')
        profile = Profile.objects.create(user=user, favorite_city='Paris')
        self.assertEqual(str(profile), 'testuser')
