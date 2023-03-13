import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rabbit.settings')

import django
django.setup()
from RabbitHole.models import Room, Post, User, Reply

import random
import string
import random

def generateContent(len):
    letters = string.ascii_lowercase
    output = ""
    for i in  range(int(random.random()*len) + 10):
        output += ''.join(random.choice(letters) for i in range(12)) + " "
    return output

def populate():

    users = [
        {"username":"reilyAdams", "email":"ReilyAdams@gmail.com", 'password':"admin"},
        {"username":"frankEvans", "email":"FrankEvans@gmail.com", 'password':"admin"},
        {"username":"masonLopez", "email":"MasonLopez@gmail.com", 'password':"admin"},
    ]

    rooms = [
        {"name":"pharmacy", 'avatar': 'default_avatars\default.png', 'creator': users[0]['username'],},
        {"name":"engineering", 'avatar': 'default_avatars\default.png', 'creator': users[0]['username']},
        {"name":"computing", 'avatar': 'default_avatars\default.png', 'creator': users[1]['username']},
        {"name":"mathematics", 'avatar': 'default_avatars\default.png', 'creator': users[1]['username']},
        {"name":"psychology", 'avatar': 'default_avatars\default.png', 'creator': users[2]['username']},
        {"name":"geography", 'avatar': 'default_avatars\default.png', 'creator': users[2]['username']}
    ]
    posts = []

    for user in users:
        add_user(user)
    
    for room in rooms:
        room_created = add_room(room)
        posts.append({"room": room_created, 'title':generateContent(25),  'content': generateContent(100), 'user': users[0]['username'], 'image' : None})
        posts.append({"room": room_created, 'title':generateContent(25),  'content': generateContent(100), 'user': users[1]['username'], 'image' : None})
        posts.append({"room": room_created, 'title':generateContent(25),  'content': generateContent(100), 'user': users[2]['username'], 'image' : None})
    
    for post in posts:
        post_created = add_post(post)
        add_reply({'post':post_created, 'title':generateContent(25), 'content': generateContent(100), 'user': users[0]['username']})
        add_reply({'post':post_created, 'title':generateContent(25), 'content': generateContent(100), 'user': users[2]['username']})
        add_reply({'post':post_created, 'title':generateContent(25), 'content': generateContent(100), 'user': users[1]['username']})

def add_user(info_dict):
    user = User.objects.create(username=info_dict['username'], email=info_dict['email'])
    user.set_password(info_dict['password'])

    user.save()

def add_room(info_dict):
    user = User.objects.get(username=info_dict['creator'])
    room = Room.objects.create(creator=user, name=info_dict['name'], avatar=info_dict['avatar'])
    members = User.objects.exclude(username=user.username)
    for member in members:
        room.participants.add(member)
    room.save()
    return room

def add_post(info_dict):
    user = User.objects.get(username=info_dict['user'])
    post = Post.objects.create(room=info_dict['room'], user=user, title=info_dict['title'], content=info_dict['content'], image=info_dict['image'])
    post.save()
    return post

def add_reply(info_dict):
    user = User.objects.get(username=info_dict['user'])
    reply = Reply.objects.create(post=info_dict['post'], user=user, title=info_dict['title'], content=info_dict['content'])
    reply.save()

if __name__ == '__main__': 

    print("Starting .....")
    populate()
    print("Completed!")
