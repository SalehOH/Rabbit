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
    avatar = models.ImageField(upload_to=user_avatar_path, default='default_avatars/default.png')
    bio = models.CharField(max_length=250, null=True)

    REQUIRED_FIELDS = ['email',]

    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return static('default_avatars/default.png')