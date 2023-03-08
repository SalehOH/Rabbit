from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Room, Post

User = get_user_model()

def index(request):
    context = {}
    try:
        posts = Post.objects.all().order_by('-created_at')
        rooms = Room.objects.all()
        context = {'posts': posts, 'rooms': rooms}
    except:
        pass

    return render(request, 'RabbitHole/index.html', context)
