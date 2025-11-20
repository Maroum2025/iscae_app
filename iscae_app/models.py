from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUser(AbstractUser):
    tel = models.IntegerField(unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager() # Use the default UserManager or a custom one if needed




class Item(models.Model):
    name = models.CharField(max_length=30, blank=True, default="")
    description = models.CharField(max_length=200, blank=True, null=True)




