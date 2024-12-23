from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represent a postal address.

    Attributes:
        number (int): Street number of the address.
        street (str): Name of the street.
        city (str): City where the address is located.
        state (str): Two-letter state code.
        zip_code (int): Postal code of the address.
        country_iso_code (str): Three-letter ISO code for the country.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """Meta options for the Address model."""
        verbose_name_plural = 'Addresses'

    def __str__(self):
        """
        Return the address as a formatted string.

        Returns:
            str: A string combining the number and the street name.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represent a rental property.

    Attributes:
        title (str): The title or name of the property.
        address (Address): A one-to-one relation to an Address object.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the title of the rental property.

        Returns:
            str: The title of the property.
        """
        return self.title
