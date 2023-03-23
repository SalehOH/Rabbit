from django.db.models.query import QuerySet
from .models import Reply, Post, Like

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
            like = Like.objects.create(user=request.user, reply=model, isdislike=True)
        data["result"] = False
    model.save()

    data["likes"] = model.countlikes

    return data

def post_likes_status(request, models):
    if type(models) != list and type(models) != QuerySet:
        models = [models]
    if request.user.is_authenticated:
        likes = Like.objects.filter(user=request.user)
        for model in models:
            if likes.filter(post=model).exists():
                if likes.get(post=model).isdislike:
                    model.likestatus = False
                if not likes.get(post=model).isdislike:
                    model.likestatus = True
            else:
                model.likestatus = None
                
def reply_likes_status(request, models):
    if request.user.is_authenticated:
        likes = Like.objects.filter(user=request.user)
        for model in models:
            if likes.filter(reply=model).exists():
                if likes.get(reply=model).isdislike:
                    model.likestatus = False
                if not likes.get(reply=model).isdislike:
                    model.likestatus = True
            else:
                model.likestatus = None