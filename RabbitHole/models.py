from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
# Create your models here.


User = get_user_model()

def reply_image_upload_path(instance, filename):
    slug = slugify(" ".join(instance.content.split(" ")[:6]))
    return f'Rooms/{slugify(instance.post.room.name)}/Posts/{instance.post.slug}/Replies/{slug}/{filename}'

def post_image_filename(instance, filename):
    slug = slugify(" ".join(instance.content.split(" ")[:6]))

    return f"Rooms/{slugify(instance.room.name)}/Posts/{slug}/{filename}"

def room_avatar_filename(instance, filename):
    return f"Rooms/{slugify(instance.name)}/avatar/{filename}"