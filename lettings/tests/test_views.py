from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingViewsTest(TestCase):
    def setUp(self):
        address = Address.objects.create(
            number=123,
            street='Main St',
            city='Springfield',
            state='IL',
            zip_code=62701,
            country_iso_code='USA'
        )
        Letting.objects.create(
            title='Test Letting',
            address=address
        )
    
    def test_index_view(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_view(self):
        letting = Letting.objects.first()
        response = self.client.get(reverse('lettings:letting', args=[letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        