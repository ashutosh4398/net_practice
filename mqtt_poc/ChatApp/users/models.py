from enum import unique

from common.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser, BaseModel):
    email = models.EmailField(unique=True, max_length=254)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def __str__(self):
        return self.username
