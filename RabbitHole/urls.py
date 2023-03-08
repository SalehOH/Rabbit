from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    #path('u/<username>/', views.user, name='user_page'),
    path('create-room/', views.create_room, name='create_room'),
    path('r/<room_name>/', views.room, name='room'),
    path('<room_name>/<user_id>/join/', views.join_room, name='join_room'),
    path('<room_name>/create-post/', views.create_post, name='create_post'),
    path('<room_name>/<post_id>/<post_slug>/', views.post, name='post'),
    path('<room_name>/<post_id>/<post_slug>/create-reply/', views.create_reply, name='create_reply'),
]