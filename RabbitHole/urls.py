from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('u/<username>/', views.user, name='user_page'),
    path('create-room/', views.create_room, name='create_room'),
    path('r/<room_name>/', views.room, name='room'),
    path('<room_name>/<user_id>/join/', views.join_room, name='join_room'),
    path('<room_name>/create-post/', views.create_post, name='create_post'),
    path('<room_name>/<post_id>/<post_slug>/', views.post, name='post'),
    path('<room_name>/<post_id>/<post_slug>/create-reply/', views.create_reply, name='create_reply'),
    path('<room_name>/delete_post/<post_id>/', views.delete_post, name='delete_post'),
    path('<room_name>/<post_id>/<post_slug>/delete_reply/<reply_id>/', views.delete_reply, name='delete_reply'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike_post/<int:post_id>/', views.dislike_post, name='dislike_post'),
    path('logout/', views.logout_view, name='logout'),
]