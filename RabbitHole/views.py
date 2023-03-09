from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages


from .models import Room, Post,Reply
from .forms import RoomForm, PostForm, ReplyForm

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

    return render(request, 'RabbitHole/create.html', {'form': form, 'name':'Room',})



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



def post(request, room_name, post_id, post_slug):
    post = get_object_or_404(Post, id=post_id, room__name=room_name, slug=post_slug)
    replies = post.replies.all().order_by('-created_at')

    context = {'post': post, 'replies': replies}
    return render(request, 'RabbitHole/post.html', context)


@login_required
def create_post(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.room = room
            post.user = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post', room_name=room_name, post_id=post.id, post_slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'RabbitHole/create.html', {'form': form, 'room': room, 'name':'Post',})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.user == post.user :
        post.delete()
        response = redirect('room',room_name=post.room.name)
    else:
        response = redirect('home')
    return response


@login_required
def create_reply(request, room_name, post_id, post_slug):
    post = get_object_or_404(Post, id=post_id, room__name=room_name, slug=post_slug)
    if request.method == 'POST':
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.user = request.user
            reply.save()
            messages.success(request, 'Reply created successfully!')
            return redirect('post', room_name=room_name, post_id=post.id,  post_slug=post.slug)
    else:
        form = ReplyForm()
    return render(request, 'RabbitHole/create.html', {'form': form, 'post': post, 'name':'Reply',})

@login_required
def delete_reply(request, reply_id):
     reply = get_object_or_404(Reply,id = reply_id)
     if reply :
         post = reply.post
         if reply.user == request.user :
             reply.delete()
         response = redirect('post',room_name = post.room.name, post_id = post.id, post_slug = post.slug)
     else:
         response = redirect('home')
     return response

def user(request, username):
    user = get_object_or_404(User, username=username)

    posts = Post.objects.filter(user=user)

    context = {'user': user,'posts': posts,}
    return render(request, 'RabbitHole/user.html', context)