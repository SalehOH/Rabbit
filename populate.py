import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rabbit.settings')

import django
django.setup()
from RabbitHole.models import Room, Post, User, Reply
from django.templatetags.static import static

import random
import string
import random



postDict = {
"Top 10 Most Prescribed Medications": "In this post, we'll explore the top 10 most commonly prescribed medications, including their uses, side effects, and potential interactions with other drugs. We'll also discuss best practices for medication management and how pharmacists can play a key role in ensuring patient safety.",
"Pharmacists' Role in Patient Care": "Pharmacists are often the first point of contact for patients seeking healthcare advice. In this post, we'll examine the various ways in which pharmacists can improve patient care, from conducting medication reviews to providing counseling on lifestyle changes. We'll also discuss the importance of interdisciplinary collaboration in achieving better health outcomes.",
"Breaking Down Drug Interactions": "With so many medications available, it's not uncommon for patients to take multiple drugs at the same time. However, some combinations can lead to dangerous interactions. In this post, we'll take a closer look at the mechanisms behind drug interactions and provide tips for minimizing their risks.",
"The Future of Robotics": "From self-driving cars to surgical robots, robotics technology is advancing rapidly. In this post, we'll explore some of the most exciting developments in the field of robotics and discuss the potential impact they could have on our lives.",
"Innovations in Sustainable Energy": "As the world becomes more conscious of the impact of climate change, sustainable energy sources are gaining popularity. In this post, we'll examine some of the latest innovations in sustainable energy, from solar power to wind turbines, and discuss their potential to create a more sustainable future.",
"Designing Safer Transportation": "Transportation is a key aspect of modern life, but it can also be dangerous. In this post, we'll explore some of the latest developments in transportation safety, from autonomous vehicles to improved infrastructure. We'll also discuss the role of engineering in designing safer transportation systems.",
"Artificial Intelligence and Ethics": "As AI becomes more prevalent in our daily lives, questions around its ethical implications are becoming increasingly important. In this post, we'll examine some of the ethical dilemmas posed by AI and discuss possible solutions.",
"Cybersecurity Threats and Solutions": "In a world where almost everything is connected to the internet, cybersecurity is more important than ever. In this post, we'll take a closer look at some of the most common cybersecurity threats, from phishing to ransomware, and discuss strategies for protecting yourself and your data.",
"The Power of Big Data": "In the age of information, data is king. In this post, we'll explore the concept of big data and how it's being used to drive innovation across a variety of industries. We'll also discuss the potential ethical implications of big data and the need for responsible data governance.",
"Applications of Calculus in Real Life": "Calculus is often considered one of the most challenging branches of mathematics, but its applications in the real world are vast. In this post, we'll explore some of the ways in which calculus is used to model and solve real-world problems, from optimizing business operations to designing spacecraft trajectories.",
"Exploring Number Theory": "Number theory is the study of the properties and relationships of numbers, and it has been a cornerstone of mathematics for centuries. In this post, we'll take a closer look at some of the key concepts in number theory, from prime numbers to modular arithmetic, and discuss their applications in fields such as cryptography and computer science.",
"The Fascinating World of Topology": "Topology is the study of the properties of objects that remain unchanged when they are stretched or deformed. In this post, we'll explore some of the fascinating ideas and concepts in topology, from the Möbius strip to the Poincaré conjecture, and discuss their applications in fields such as physics and computer science.",
"Understanding the Human Mind: A Comprehensive Overview": "Psychology is the scientific study of human behavior and mental processes, and it encompasses a wide range of topics and theories. In this post, we'll provide a comprehensive overview of psychology, from its historical roots to modern-day applications in areas such as therapy and education.",
"Theories of Personality Development": "Personality development is a complex and multifaceted process that has been the subject of study in psychology for many years. In this post, we'll explore some of the key theories of personality development, from Freud's psychoanalytic theory to Maslow's hierarchy of needs.",
"The Effects of Trauma on Mental Health": "Trauma can have a profound impact on an individual's mental health, and it can manifest in a variety of ways. In this post, we'll examine the different types of trauma and their effects on mental health, from post-traumatic stress disorder to complex trauma.",
"Climate Change and its Impact on the World": "Climate change is one of the most pressing issues facing the world today, and its impact is being felt in various ways. Rising global temperatures are causing more frequent and severe weather events such as hurricanes, droughts, and wildfires, which are affecting communities and economies around the world.",
"Exploring Biodiversity Hotspots": "Biodiversity hotspots are areas with exceptionally high levels of species diversity and endemism, meaning that many of the species found there are not found anywhere else in the world. In this post, we'll explore some of the most important biodiversity hotspots around the world and discuss why they are so important for conservation efforts.",
"The Importance of Mapping": "Mapping is a critical tool for understanding and managing our world. In this post, we'll examine the importance of mapping in fields such as geography, urban planning, and emergency response. We'll also explore some of the latest advances in mapping technology, from drones to satellite imagery."}

titles = {
  "pharmacy": ["Top 10 Most Prescribed Medications", "Pharmacists' Role in Patient Care", "Breaking Down Drug Interactions"],
  "engineering": ["The Future of Robotics", "Innovations in Sustainable Energy", "Designing Safer Transportation"],
  "computing": ["Artificial Intelligence and Ethics", "Cybersecurity Threats and Solutions", "The Power of Big Data"],
  "mathematics": ["Applications of Calculus in Real Life", "Exploring Number Theory", "The Fascinating World of Topology"],
  "psychology": ["Understanding the Human Mind: A Comprehensive Overview", "Theories of Personality Development", "The Effects of Trauma on Mental Health"],
  "geography": ["Climate Change and its Impact on the World", "Exploring Biodiversity Hotspots", "The Importance of Mapping"]
}

reply = ["Absolutely!","That's exactly how I feel too.","I couldn't agree more.","You read my mind!","I'm completely on board with that.","I share your perspective.","I'm in complete agreement with you.","Yes, yes, yes!","You've hit the nail on the head.","That's precisely what I was thinking.","I couldn't have said it better myself.","You've got my vote.","I'm with you 100%.","You're speaking my language.","That's music to my ears.","You're preaching to the choir.","That's a great point, I totally agree.","I couldn't disagree with you if I tried.","I'm fully supportive of that.","I'm right there with you.","Spot on!","You're absolutely right.","That's a fantastic idea, count me in.","Your opinion aligns perfectly with mine.","I'm completely in favor of that.","You've convinced me, I agree.","That's precisely how I see it too.","You've captured my thoughts exactly.","You're reading my mind.","I couldn't have said it any better.","Sorry, I don't have time for this right now.","I'm not interested in your proposal.","Your idea is completely ridiculous.","Why would I want to waste my time on that?","I have no desire to work with you.","Your argument makes no sense.","I have no faith in your abilities.","That's the dumbest thing I've ever heard.","I have more important things to do than listen to you.","Your suggestion is completely impractical.","I don't think you have the necessary skills to make this happen.","That's not a feasible solution.","I don't think you understand the situation.","I don't have any confidence in your plan.","That's a terrible idea.","I don't think you have thought this through.","Your approach is completely flawed.","Your proposal is a waste of my time.","I don't trust you to execute this properly.","Your logic is completely flawed.","I have no interest in what you're proposing.","Your idea is completely unworkable.","That's a ridiculous suggestion.","I don't think you're capable of making this happen.","I'm not going to waste my time on your proposal.","Your plan is completely unrealistic.","That's not going to work.","I don't think you have the necessary experience to make this happen.","Your idea is not well thought out.","Sorry, but I'm not interested in what you're proposing."]


def populate():

    users = [
    {"username": "reilyAdams", "email": "ReilyAdams@gmail.com", "password": "admin", "avatar": "{% static 'default_avatars/peach.png' %}"},
    {"username": "frankEvans", "email": "FrankEvans@gmail.com", "password": "admin", "avatar": "{% static 'default_avatars/mario.png' %}"},
    {"username": "masonLopez", "email": "MasonLopez@gmail.com", "password": "admin", "avatar": "{% static 'default_avatars/luigi.png' %}"}
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
        posts.append({"room": room_created, 'title':titles[room_created.name][0],  'content': postDict[titles[room_created.name][0]], 'user': users[0]['username'], 'image' : None})
        posts.append({"room": room_created, 'title':titles[room_created.name][1],  'content': postDict[titles[room_created.name][1]], 'user': users[1]['username'], 'image' : None})
        posts.append({"room": room_created, 'title':titles[room_created.name][2],  'content': postDict[titles[room_created.name][2]], 'user': users[2]['username'], 'image' : None})
    
    for post in posts:
        post_created = add_post(post)
        for i in range(random.randint(2,9)):
            replyIndex = random.randint(0,59)
            add_reply({'post':post_created, 'title':reply[replyIndex], 'content':reply[replyIndex], 'user': users[random.randint(0, 2)]['username']})


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
