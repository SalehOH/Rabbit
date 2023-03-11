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

class Room(models.Model):
    name = models.CharField(_("name"), max_length=30, unique=True,)
    avatar = models.ImageField(upload_to=room_avatar_filename)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_rooms')

    participants = models.ManyToManyField(User, related_name='rooms_participated_in')

    def __str__(self):
        return self.name
    
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to=post_image_filename, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    slug= models.SlugField(default='',null=True)
    countlikes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(" ".join(self.content.split(" ")[:6]))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
         return " ".join(self.content.split(" ")[:3])
    
class Reply(models.Model):
    content = models.TextField(max_length=300, null=False, blank=False)
    image = models.ImageField(upload_to=reply_image_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    slug = models.SlugField(default='',null=True)
    countlikes = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'replies'

    def save(self, *args, **kwargs):
        self.slug = slugify(" ".join(self.content.split(" ")[:6]))
        super(Reply, self).save(*args, **kwargs)

    def __str__(self):
        return " ".join(self.content.split(" ")[:2])
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', null=True)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='likes', null=True)
    isdislike = models.BooleanField(default=False)


    class Meta:
        unique_together = ('user', 'post')
        unique_together = ('user', 'reply')