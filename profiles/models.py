from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (User): A one-to-one relationship with the User model.
        favorite_city (str): The user's favorite city, optional.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return the username of the profile's user.

        Returns:
            str: The username associated with the profile.
        """
        return self.user.username
