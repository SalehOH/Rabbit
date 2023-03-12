from django import forms
from .models import Room, Post, Reply


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'avatar',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'content': forms.Textarea(attrs={'class': 'form-control textF', 'data-type': 'text'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file imageF', 'data-type': 'picture'}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
