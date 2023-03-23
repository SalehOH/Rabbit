from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Q, Count

from .models import Room, Post, Reply, Like
from .forms import RoomForm, PostForm, ReplyForm, UserForm
from .helper import like_helper, dislike_helper, post_likes_status, reply_likes_status

User = get_user_model()

def index(request):
    rooms = Room.objects.annotate(members=Count('participants')).order_by('-members')
    q = request.GET.get('q')
    
    if q:
        if q == 'hot':
            posts = Post.objects.annotate(num_replies=Count('replies')).order_by('-num_replies')
        elif q == 'new':
            posts = Post.objects.all().order_by('-created_at')
    else:
        if not request.user.is_anonymous:
            posts = Post.objects.filter(room__in=Room.objects.filter(
                Q(participants__id=request.user.id) |
                Q(creator=request.user)
            ))
            if len(posts) < 1:
                posts = Post.objects.all()
        else:
            posts = Post.objects.all()
        posts = posts.order_by('-created_at')

    post_likes_status(request, posts)
    context = {'posts': posts, 'rooms': rooms, 'page': 'home'}
    return render(request, 'RabbitHole/index.html', context)

def search(request):
    query = request.GET.get('q')
    users = User.objects.filter(username__icontains=query).values('username', 'avatar')
    rooms = Room.objects.filter(name__icontains=query).values('name', 'avatar')

    data = {'users': list(users), 'rooms': list(rooms)}
    return JsonResponse(data)

def room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    context = {'room': room, 'page': 'room'}
    try:
        posts = Post.objects.filter(room=room)
        context['posts'] = posts
    except:
        pass
    post_likes_status(request, posts)
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

    post_likes_status(request, post)
    reply_likes_status(request, replies)

    context = {'post': post, 'replies': replies}
    return render(request, 'RabbitHole/post.html', context)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = like_helper(request,post,'post')
    return JsonResponse(data)

@login_required
def dislike_post(request, post_id): 
    post = get_object_or_404(Post, id=post_id)
    data = dislike_helper(request, post, 'post')
    return JsonResponse(data)

@login_required
def like_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    data = like_helper(request,reply,'reply')
    return JsonResponse(data)

@login_required
def dislike_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    data = dislike_helper(request, reply, 'reply')
    return JsonResponse(data)

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
    room_name = post.room.name
    if request.user == post.user :
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        if len(request.META.get('HTTP_REFERER')[7:].split("/")) >=5:
            response = redirect('room', room_name)
        else:
            response = redirect(request.META.get('HTTP_REFERER'))
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
         if reply.user == request.user :
             reply.delete()
             messages.success(request, 'Reply deleted successfully!')
         response = redirect(request.META.get('HTTP_REFERER'))
     else:
         response = redirect('home')
     return response

def user(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    post_likes_status(request, posts)
    context = {'user': user,'posts': posts,}
    return render(request, 'RabbitHole/user.html', context)

@login_required 
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        if request.method == 'POST':
           form = UserForm(request.POST, request.FILES, instance=user)
           if form.is_valid():
               form.save()
               return redirect('user_page', username)
        else:
           form = UserForm(instance=user)

    return render(request, 'RabbitHole/edit_profile.html', {'form': form})