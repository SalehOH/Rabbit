from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Q, Count

from .models import Room, Post, Reply, Like
from .forms import RoomForm, PostForm, ReplyForm

User = get_user_model()

def index(request):
    rooms = Room.objects.annotate(members=Count('participants')).order_by('-members')
    
    if not request.user.is_anonymous:
        posts = Post.objects.filter(room__in=Room.objects.filter(
            Q(participants__id=request.user.id) |
            Q(creator=request.user)
        )).annotate(num_replies=Count('replies')).order_by('-created_at')
        if len(posts) < 2:
            posts = Post.objects.all().annotate(num_replies=Count('replies')).order_by('-created_at')
    else:
        posts = Post.objects.all().annotate(num_replies=Count('replies')).order_by('-created_at')
    
    context = {'posts': posts, 'rooms': rooms, 'page': 'home'}

    if request.user.is_authenticated:
        likes = Like.objects.filter(user=request.user)
        for post in posts:
            if likes.filter(post=post).exists():
                if likes.get(post=post).isdislike:
                    post.likestatus = False
                if not likes.get(post=post).isdislike:
                    post.likestatus = True
            else:
                post.likestatus = None
                
            post.num_replies = post.num_replies

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
    
    return render(request, 'RabbitHole/room.html', context)




@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save(commit=False)
            room.creator = request.user
            room.save()
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

    rooms = Room.objects.annotate(members=Count('participants')).order_by('-members')
    replies = post.replies.all().order_by('-created_at')

    context = {'post': post, 'replies': replies, 'rooms': rooms}

    likes = Like.objects.filter(user=request.user)
    if likes.filter(post=post).exists():
        if likes.get(post=post).isdislike:
            post.likestatus = False
        if not likes.get(post=post).isdislike:
            post.likestatus = True
    else:
        post.likestatus = None

    for reply in replies:
        if likes.filter(reply=reply).exists():
            if likes.get(reply=reply).isdislike:
                reply.likestatus = False
            if not likes.get(reply=reply).isdislike:
                reply.likestatus = True
        else:
            reply.likestatus = None

    post.num_replies = post.replies.count()

    return render(request, 'RabbitHole/post.html', context)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = like_helper(request,post,'post')
    #try:
    #    like = post.likes.get(user=request.user)
    #    if like.isdislike:
    #        post.countlikes += 2
    #        like.isdislike = False
    #        data["result"] = True
    #        like.save()
    #    else:
    #        post.countlikes -= 1
    #        like.delete()
    #        data["result"] = None
    #except Like.DoesNotExist:
    #    post.countlikes += 1
    #    like = Like.objects.create(user=request.user, post=post)
    #    data["result"] = True
    #post.save()
#
    #data["likes"] = post.countlikes
    return JsonResponse(data)

@login_required
def dislike_post(request, post_id): 
    post = get_object_or_404(Post, id=post_id)
    data = dislike_helper(request, post, 'post')
    #try:
    #    like = post.likes.get(user=request.user)
    #    if not like.isdislike:
    #        post.countlikes -= 2
    #        like.isdislike = True
    #        data["result"] = False
    #        like.save()
    #    else:
    #        post.countlikes += 1
    #        like.delete()
    #        data["result"] = None
    #except Like.DoesNotExist:
    #    post.countlikes -= 1
    #    like = Like.objects.create(user=request.user, post=post, isdislike=True)
    #    data["result"] = False
    #post.save()
    #
    #data["likes"] = post.countlikes

    return JsonResponse(data)

@login_required
def like_reply(request, reply_id):
    data = {}
    reply = get_object_or_404(Reply, id=reply_id)
    try:
        like = reply.likes.get(user=request.user)
        if like.isdislike:
            reply.countlikes += 2
            like.isdislike = False
            data["result"] = True
            like.save()
        else:
            reply.countlikes -= 1
            like.delete()
            data["result"] = None
    except Like.DoesNotExist:
        reply.countlikes += 1
        like = Like.objects.create(user=request.user, reply=reply)
        data["result"] = True
    reply.save()

    data["likes"] = reply.countlikes



    return JsonResponse(data)

@login_required
def dislike_reply(request, reply_id):
    data = {}
    reply = get_object_or_404(Reply, id=reply_id)
    try:
        like = reply.likes.get(user=request.user)
        if not like.isdislike:
            reply.countlikes -= 2
            like.isdislike = True
            data["result"] = False
            like.save()
        else:
            reply.countlikes += 1
            like.delete()
            data["result"] = None
    except Like.DoesNotExist:
        reply.countlikes -= 1
        like = Like.objects.create(user=request.user, reply=reply, isdislike=True)
        data["result"] = False
    reply.save()

    data["likes"] = reply.countlikes

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
    if request.user == post.user :
        post.delete()
        messages.success(request, 'Post deleted successfully!')
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
         post = reply.post
         if reply.user == request.user :
             reply.delete()
             messages.success(request, 'Reply deleted successfully!')
         response = redirect(request.META.get('HTTP_REFERER'))
     else:
         response = redirect('home')
     return response

def user(request, username):
    user = get_object_or_404(User, username=username)

    posts = Post.objects.filter(user=user)

    context = {'user': user,'posts': posts,}
    return render(request, 'RabbitHole/user.html', context)

def like_helper(request,model, name):
    data = {}
    try:
        like = model.likes.get(user=request.user)
        if like.isdislike:
            model.countlikes += 2
            like.isdislike = False
            data["result"] = True
            like.save()
        else:
            model.countlikes -= 1
            like.delete()
            data["result"] = None
    except Like.DoesNotExist:
        model.countlikes += 1
        if name == 'post':
            like = Like.objects.create(user=request.user, post=model)
        else:
             like = Like.objects.create(user=request.user, reply=model)
        data["result"] = True
    model.save()
    data["likes"] = model.countlikes
    return data

def dislike_helper(request, model, name):
    data = {}
    try:
        like = model.likes.get(user=request.user)
        if not like.isdislike:
            model.countlikes -= 2
            like.isdislike = True
            data["result"] = False
            like.save()
        else:
            model.countlikes += 1
            like.delete()
            data["result"] = None
    except Like.DoesNotExist:
        model.countlikes -= 1
        if name == 'post':
            like = Like.objects.create(user=request.user, post=model, isdislike=True)
        else:
            like = Like.objects.create(user=request.user, room=model, isdislike=True)
        data["result"] = False
    model.save()

    data["likes"] = model.countlikes

    return data