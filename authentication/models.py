from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    name = None
    email = models.EmailField(unique=True, null=False)
    bio = models.CharField(max_length=250, null=True)

    REQUIRED_FIELDS = ['email',]