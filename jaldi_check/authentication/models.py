from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    address = models.TextField()


class RealEstate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_real_estate", null=True)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=255)
    real_estate_address = models.TextField()
