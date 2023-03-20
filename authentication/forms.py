from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

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
        

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your username', 'id': 'username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control','placeholder': 'Enter your password', 'id': 'password'})