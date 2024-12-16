from django.test import TestCase
from .models import Letting, Address

class LettingsModelTests(TestCase):
    
    def test_address_str(self):
        """
        Test the string representation of the Address model.
        """
        address = Address.objects.create(
            number=123,
            street='Main St',
            city='Springfield',
            state='IL',
            zip_code=62701,
            country_iso_code='USA'
        )
        self.assertEqual(str(address), '123 Main St')

    def test_letting_str(self):
        """
        Test the string representation of a Letting instance.
        """
        address = Address.objects.create(
            number=123,
            street='Main St',
            city='Springfield',
            state='IL',
            zip_code=62701,
            country_iso_code='USA'
        )
        letting = Letting.objects.create(
            title='Test Letting',
            address=address
        )
        self.assertEqual(str(letting), 'Test Letting')
