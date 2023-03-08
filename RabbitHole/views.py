from django.shortcuts import render

from .models import Room, Post

def index(request):
    context = {}
    try:
        posts = Post.objects.all().order_by('-created_at')
        rooms = Room.objects.all()
        context = {'posts': posts, 'rooms': rooms}
    except:
        pass

    return render(request, 'RabbitHole/index.html', context)
