from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Our custom user model"""

    age = models.PositiveIntegerField(null= False, blank=True)