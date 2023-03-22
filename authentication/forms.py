from allauth.account.forms import SignupForm, LoginForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class CustomSocialSignupForm(SocialSignupForm):
    username = forms.CharField(label=_('Username'), max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    avatar = forms.ImageField(label='Avatar', required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control',}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.HiddenInput()
        self.fields['email'].label = ''

    def clean_username(self):
        username = self.cleaned_data['username']
        username = username.lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_('This username is already taken.'))
        return username

    def save(self, request):
        user = super(CustomSocialSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.avatar = self.cleaned_data['avatar']
        user.save()
        return user

class CustomSignupForm(SignupForm):
    avatar = forms.ImageField(label='Avatar', required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs = {
            'username': ['Enter your username', 'form-control'],
            'email': ['Enter your email', 'form-control'],
            'password1': ['Enter your password', 'form-control'],
            'password2': ['Confirm your password', 'form-control'],
            'avatar': ['Select your avatar', 'form-control'],
        }
        for field_name, field in self.fields.items():
            widget = field.widget
            if field_name in attrs and widget.input_type != 'checkbox':
                widget.attrs.update({'placeholder': attrs[field_name][0], 'class': attrs[field_name][1]})
            widget.attrs.update(attrs)
            widget.attrs.pop('autofocus', None)
    
    def save(self, request):
        user = super().save(request)
        user.avatar = self.cleaned_data['avatar']
        user.save()
        return user 

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your username', 'id': 'username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control','placeholder': 'Enter your password', 'id': 'password'})