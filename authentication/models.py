from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

def user_avatar_path(instance, filename):
    
    return f'Users/{slugify(instance.username)}/avatar/{filename}'

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    name = None
    email = models.EmailField(unique=True, null=False)
    avatar = models.ImageField(upload_to=user_avatar_path, default='default_avatars/default.png', blank=True)
    bio = models.CharField(max_length=250, null=True, blank=True)

    REQUIRED_FIELDS = ['email',]
