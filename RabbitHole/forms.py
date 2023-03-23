from django import forms
from .models import Room, Post, Reply, User


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'avatar',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Room.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('A room with this name already exists.')
        if not name.isalpha():
            raise forms.ValidationError('Room name can only contain letters.')
        if ' ' in name:
            raise forms.ValidationError('Room name cannot contain whitespace.')
        return name.lower()
    
    def clean_avatar(self):
       avatar = self.cleaned_data.get('avatar')
       if not avatar:
           raise forms.ValidationError('Please upload an avatar.')
       return avatar   

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'content': forms.Textarea(attrs={'class': 'form-control textF', 'data-type': 'text'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control imageF', 'data-type': 'picture'}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['title','content', 'image']
        widgets = {  
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'content': forms.Textarea(attrs={'class': 'form-control textF', 'data-type': 'text'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control imageF', 'data-type': 'picture'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'bio']
