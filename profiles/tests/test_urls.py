from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import profile, index


class ProfilesUrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, index)

    def test_profile_url_resolves(self):
        url = reverse('profiles:profile', args=['some-username'])
        self.assertEqual(resolve(url).func, profile)