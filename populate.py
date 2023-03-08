import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rabbit.settings')

import django
django.setup()
from RabbitHole.models import Room, Post, User

def addUser(userDict):
    user = User.objects.get_or_create(username=userDict["username"], email=userDict["email"])[0]
    user.save()
    return user

users = []
users.append({"username":"ReilyAdams", "email":"ReilyAdams@gmail.com"})
users.append({"username":"FrankEvans", "email":"FrankEvans@gmail.com"})
users.append({"username":"MasonLopez", "email":"MasonLopez@gmail.com"})

for index, user in enumerate(users):
    users[index] = addUser(user)

def addRoom(roomDict):
    room = Room.objects.get_or_create(name=roomDict["name"], creator=roomDict["user"])[0]
    room.save()
    return room

rooms = []
rooms.append({"name":"pharmacy", "user":users[0]})
rooms.append({"name":"engineering", "user":users[0]})
rooms.append({"name":"computing", "user":users[1]})
rooms.append({"name":"mathematics", "user":users[1]})
rooms.append({"name":"psychology", "user":users[2]})
rooms.append({"name":"geography", "user":users[2]})

for index, room in enumerate(rooms):
    rooms[index] = addRoom(room)

def addPost(postDict):
    post = Post.objects.get_or_create(room=postDict["room"], user=postDict["user"], content=postDict["content"])[0]
    post.save()
    return post

posts = []

content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed consequat hendrerit consequat. Praesent tortor eros, convallis eu sollicitudin sodales, efficitur a augue. Etiam quis odio sed dui venenatis dictum eget ultrices justo. Aliquam eu neque feugiat, semper lectus vel, ornare arcu. Duis vitae lectus massa. Praesent pellentesque pellentesque sem, vitae sollicitudin sem pharetra non. Pellentesque id suscipit diam. Fusce nec eros sagittis, molestie velit id, tempor urna. Etiam quis ligula in ante faucibus ullamcorper. Nunc aliquet ex et porta mattis. Pellentesque pulvinar massa volutpat rutrum consectetur. Nunc consequat pellentesque ex, a faucibus nisi fringilla nec. Mauris sodales quam sed lectus facilisis, vitae egestas odio consectetur. Mauris elementum velit et cursus mollis. Quisque odio purus, fermentum ac ante eget, pharetra elementum mi."

posts.append({"room":rooms[1], "user":users[0], "content":content})
posts.append({"room":rooms[1], "user":users[0], "content":content})
posts.append({"room":rooms[1], "user":users[0], "content":content})
posts.append({"room":rooms[1], "user":users[0], "content":content})
posts.append({"room":rooms[2], "user":users[1], "content":content})
posts.append({"room":rooms[2], "user":users[1], "content":content})
posts.append({"room":rooms[2], "user":users[1], "content":content})
posts.append({"room":rooms[2], "user":users[1], "content":content})
posts.append({"room":rooms[3], "user":users[2], "content":content})
posts.append({"room":rooms[3], "user":users[2], "content":content})
posts.append({"room":rooms[3], "user":users[2], "content":content})
posts.append({"room":rooms[3], "user":users[2], "content":content})

for index, post in enumerate(posts):
    posts[index] = addPost(post)


if __name__ == '__main__': #beginning of execution
    populate()