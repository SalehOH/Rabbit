from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages


from .models import Room, Post
from .forms import RoomForm

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

def room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    context = {'room': room,}
    try:
        posts = Post.objects.filter(room=room)
        context['posts'] = posts
    except:
        pass
    
    return render(request, 'RabbitHole/room.html', context)




@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.creator = request.user
            room.save()
            room.participants.add(request.user)
            messages.success(request, 'Room created successfully!')
            return redirect('room', room_name=room.name)
    else:
        form = RoomForm()

    return render(request, 'RabbitHole/create.html', {'form': form,})

@login_required
def join_room(request, room_name, user_id):
    room = get_object_or_404(Room, name=room_name)
    user = get_object_or_404(User, id=user_id)
    if room:
        if room.creator.id == user_id or user in room.participants.all():
            return redirect('room', room_name=room_name)
        
        else:
            room.participants.add(user)
            messages.success(request, f"You have joined '{room_name}'!")
            return redirect('room', room_name=room_name)
    else:
        redirect('home')