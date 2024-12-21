from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address
import logging
from unittest.mock import patch

logger = logging.getLogger(__name__)


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


    def test_index_view_logs_error(self):
        """
        Test that an exception in the index view is logged and raised.
        """
        # Simuler une exception sur Letting.objects.all()
        with patch('lettings.models.Letting.objects.all', side_effect=Exception("Test exception")):
            with self.assertLogs('lettings.views', level='ERROR') as log:
                # Vérifier que l'exception est levée
                with self.assertRaises(Exception):
                    self.client.get(reverse('lettings:index'))
                # Vérifier que le message d'erreur est bien dans les logs
                self.assertTrue(
                    any("Error in lettings index view: Test exception" in message for message in log.output)
                )

    def test_letting_view_logs_error(self):
        """
        Test that the letting view logs an error and raises an exception if an error occurs.
        """
        invalid_id = 9999  # ID inexistant
        # Mock Letting.objects.get to raise an exception
        with patch('lettings.models.Letting.objects.get', side_effect=Exception("Test exception")):
            with self.assertLogs('lettings.views', level='ERROR') as log:
                # Check if the exception is raised
                with self.assertRaises(Exception):
                    self.client.get(reverse('lettings:letting', args=[invalid_id]))
                # Verify the log message contains the expected error
                self.assertTrue(
                    any("Error in lettings letting view: Test exception" in message for message in log.output),
                    f"Actual logs: {log.output}"
                )






    