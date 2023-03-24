from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
User = get_user_model()
class TestAuthentication(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('account_signup')
        self.login_url = reverse('account_login')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_model = get_user_model()

    def test_signup_without_email(self):
        User.objects.filter(username='testuser').delete()
        username = 'testuser'
        password = 'test@2112password'
        avatar_file = SimpleUploadedFile(name='test_image.jpg', content=open("MediaContent\default_avatars\srobots.jpg", 'rb').read(), content_type='image/jpeg')
        
        data = {
            'username': username,
            'password1': password,
            'password2': password,
            'avatar': avatar_file
        }

        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 302)

        user = self.user_model.objects.get(username=username)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)
        self.assertFalse(user.email)
        self.assertIsNotNone(user.avatar)

    def test_login(self):
        data = {
            'login': self.user.username,
            'password': 'testpass',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))


class TestAllauthTemplates(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('account_signup')
        self.login_url = reverse('account_login')

    def test_signup_template(self):
        response = self.client.get(self.signup_url)
        self.assertContains(response, '<div class="card-header text-center">Sign up with Rabbit</div>')
        self.assertContains(response, ' <form class="signup" id="signup_form" enctype="multipart/form-data" method="post" action="/accounts/signup/">')
        self.assertContains(response, 'id="signup_form"')
        self.assertContains(response, 'id="id_username"')
        self.assertContains(response, 'id="id_email"')
        self.assertContains(response, 'id="id_password1"')
        self.assertContains(response, 'id="id_password2"')
        self.assertContains(response, '<button type="submit" class="w-50 btn btn-lg btn-outline-primary text-center">Sign up</button>')

    def test_login_template(self):
        response = self.client.get(self.login_url)
        self.assertContains(response, '<div class="card-header text-center">Login with Rabbit</div>')
        self.assertContains(response, '<form class="login" id="signup_form" method="post" action="/accounts/login/">')
        self.assertContains(response, 'id="username"')
        self.assertContains(response, 'id="password"')
        self.assertContains(response, '<button type="submit" class="w-50 btn btn-lg btn-outline-primary text-center">Login</button>')
        