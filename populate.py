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
"Top 10 Most Prescribed Medications": "Medications play an essential role in treating various medical conditions, from chronic diseases to acute illnesses. In this post, we'll dive into the top 10 most commonly prescribed medications and explore their uses, dosages, side effects, and potential drug interactions. We'll also provide practical tips for medication management, including how to take medications safely and effectively, and why it's important to communicate with your healthcare provider about any changes in your medication regimen. Additionally, we'll highlight the crucial role pharmacists play in ensuring patient safety and how they can help patients manage their medications more efficiently."
,"Pharmacists' Role in Patient Care": "As the medication experts on the healthcare team, pharmacists have a critical role to play in optimizing patient care. In this post, we'll explore the various ways in which pharmacists can contribute to improving patient outcomes, from conducting medication reviews to counseling on lifestyle modifications, such as diet and exercise. We'll also examine the importance of interdisciplinary collaboration in delivering comprehensive care and discuss how pharmacists can work alongside other healthcare professionals to achieve better health outcomes for patients. Additionally, we'll highlight the essential role pharmacists play in medication safety, including how they can help patients avoid medication errors and adverse drug reactions."
,"Breaking Down Drug Interactions": "When it comes to medication, safety is paramount. However, with so many drugs available, it's not uncommon for patients to take multiple medications simultaneously, which can increase the risk of drug interactions. In this post, we'll take a deep dive into the mechanisms behind drug interactions, including how medications can interact with each other and with certain foods, supplements, and herbal products. We'll also provide practical tips for minimizing the risk of drug interactions, including the importance of disclosing all medications to your healthcare provider and pharmacist. Additionally, we'll examine some of the most common drug interactions and how they can impact patients' health."
,"The Future of Robotics": "Robotics technology is rapidly advancing, and its potential impact on our lives is vast. In this post, we'll explore some of the most exciting developments in the field of robotics, from self-driving cars to surgical robots. We'll examine the benefits and challenges of these technologies, including their potential to improve efficiency, safety, and accessibility in various industries. Additionally, we'll discuss the ethical considerations surrounding the use of robotics and how policymakers can balance innovation with regulation to ensure responsible development and deployment of these technologies."
,"Innovations in Sustainable Energy": "As the world faces increasing environmental challenges, the demand for sustainable energy sources continues to grow. In this post, we'll explore some of the latest innovations in sustainable energy, from solar power to wind turbines, and examine how these technologies can help mitigate climate change and promote a more sustainable future. We'll also discuss the economic and social implications of transitioning to renewable energy sources and how governments and businesses can work together to accelerate the shift towards a low-carbon economy. Additionally, we'll examine some of the challenges facing the adoption of sustainable energy, including the need for infrastructure improvements and the role of public policy in incentivizing sustainable energy development."
,"Designing Safer Transportation": "Transportation is an essential part of modern life that enables people to travel to work, school, and other places. However, the rise in traffic accidents and fatalities has led to the need for safer transportation systems. In this post, we'll delve into some of the latest developments in transportation safety, including advanced driver-assistance systems (ADAS), intelligent transportation systems (ITS), and improved infrastructure. We'll also discuss the critical role that engineering plays in designing and developing safer transportation systems that prioritize passenger safety and reduce the number of accidents on the roads."
,"Artificial Intelligence and Ethics": "As artificial intelligence (AI) continues to infiltrate various aspects of our daily lives, ethical implications surrounding its use have become increasingly important. In this post, we'll delve into some of the ethical dilemmas posed by AI, including concerns around privacy, bias, and accountability. We'll also discuss some of the possible solutions that have been proposed, including ethical guidelines and regulations, and examine how they could be implemented to ensure the responsible and ethical development of AI."
,"Cybersecurity Threats and Solutions": "The increasing prevalence of digital technologies in our daily lives has made cybersecurity more critical than ever. In this post, we'll take a closer look at some of the most common cybersecurity threats, including phishing attacks, malware, and ransomware, and discuss strategies for protecting yourself and your data. We'll also explore some of the latest cybersecurity solutions, such as multi-factor authentication, endpoint security, and threat intelligence, and discuss how they can be used to prevent cyber attacks and minimize damage in case of a breach."
,"The Power of Big Data": "In the era of big data, the collection, analysis, and interpretation of massive amounts of data have transformed the way organizations make decisions and drive innovation. In this post, we'll explore the concept of big data and its potential applications in various industries, including healthcare, finance, and marketing. We'll also discuss the potential ethical implications of big data and the need for responsible data governance to ensure that the collection and use of data is done in a way that is both ethical and legal."
,"Applications of Calculus in Real Life": "Calculus is a branch of mathematics that provides tools for modeling and solving problems that involve change and rates. In this post, we'll explore some of the ways in which calculus is used in the real world, including optimization problems in business and engineering, physics and astronomy, and even in the study of the spread of infectious diseases. We'll also discuss some of the challenges involved in applying calculus to real-world problems and how it can be used to generate meaningful insights."
,"Exploring Number Theory": "Number theory is a branch of mathematics that deals with the properties and relationships of numbers, including prime numbers, divisibility, and modular arithmetic. In this post, we'll take a closer look at some of the key concepts in number theory and their applications in fields such as cryptography, computer science, and data science. We'll also examine some of the unsolved problems in number theory and the ongoing efforts to solve them."
,"The Fascinating World of Topology": "Topology is a branch of mathematics that studies the properties of objects that remain invariant under certain types of transformations, such as stretching, bending, or twisting. In this post, we'll explore some of the fascinating ideas and concepts in topology, including the concepts of continuity, connectedness, and dimensionality. We'll also discuss some of the applications of topology in fields such as physics, computer science, and even art and design, and how it has helped researchers gain a deeper understanding of the nature of space and geometry."
,"Understanding the Human Mind: A Comprehensive Overview": "Psychology is a vast field that seeks to understand the workings of the human mind and behavior. This field has undergone significant development since its inception, with various theories, approaches, and methodologies emerging. The historical roots of psychology can be traced back to the ancient Greeks, who studied human behavior through philosophy. However, modern psychology emerged in the late 19th century as a scientific discipline, thanks to the works of pioneers such as Wilhelm Wundt, Sigmund Freud, and Ivan Pavlov. Today, psychology has numerous applications, ranging from clinical therapy and counseling to education, sports, and business."
,"Theories of Personality Development": "Personality development is a fascinating and complex process that has been the subject of study in psychology for decades. Personality refers to an individual's characteristic patterns of thoughts, feelings, and behaviors that make them unique. Theories of personality development attempt to explain how individuals acquire their personality traits and how these traits evolve over time. One of the earliest and most influential theories of personality development is Freud's psychoanalytic theory, which posits that personality is shaped by unconscious conflicts and experiences during childhood. Other theories of personality development include Maslow's hierarchy of needs, which suggests that individuals are motivated by a hierarchy of needs that range from basic physiological needs to self-actualization."
,"The Effects of Trauma on Mental Health": "Trauma is a pervasive and distressing experience that can have long-lasting effects on an individual's mental health. Trauma can occur in many forms, including physical, emotional, sexual, or psychological abuse, war, natural disasters, accidents, or witnessing violence. The effects of trauma on mental health can be severe and vary from individual to individual. Some people may develop post-traumatic stress disorder (PTSD), which is characterized by intrusive thoughts, flashbacks, and avoidance behaviors. Others may experience complex trauma, which results from repeated and prolonged exposure to trauma and can lead to a range of mental health disorders, including depression, anxiety, and dissociative disorders."
,"Climate Change and its Impact on the World": "Climate change is an existential threat that has far-reaching consequences for the planet's ecosystems, economies, and communities. Climate change is caused by human activities such as burning fossil fuels, deforestation, and agriculture, which release greenhouse gases into the atmosphere and trap heat, leading to rising global temperatures. The impact of climate change is already being felt in various ways, from more frequent and severe weather events such as hurricanes, droughts, and wildfires to rising sea levels and loss of biodiversity. Climate change also exacerbates existing social and economic inequalities, affecting vulnerable populations such as low-income communities, indigenous peoples, and developing countries."
,"Exploring Biodiversity Hotspots": "Biodiversity hotspots are areas with exceptional levels of species diversity and endemism, making them critical for conservation efforts. These areas are typically concentrated in tropical regions and island ecosystems, where environmental conditions have allowed for the evolution of unique and diverse species. Biodiversity hotspots are essential for maintaining ecosystem functioning and providing ecosystem services such as pollination, water filtration, and carbon sequestration. However, biodiversity hotspots are also under threat due to human activities such as deforestation, habitat fragmentation, and climate change. Protecting biodiversity hotspots is therefore crucial for preserving the planet's biodiversity and mitigating the effects of climate change."
,"The Importance of Mapping": "Mapping plays a critical role in fields such as geography, urban planning, and emergency response. In geography, maps are used to study and understand the distribution of natural and human-made features such as rivers, mountains, cities, and transportation networks. Urban planners use maps to design cities and plan for the distribution of resources and infrastructure such as housing, transportation, and parks. In emergency response, maps are used to identify areas at risk of natural disasters such as floods and earthquakes and to plan evacuation routes and rescue operations"
}

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
    {"username": "reilyAdams", "email": "ReilyAdams@gmail.com", "password": "admin"},
    {"username": "frankEvans", "email": "FrankEvans@gmail.com", "password": "admin"},
    {"username": "masonLopez", "email": "MasonLopez@gmail.com", "password": "admin"}
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
