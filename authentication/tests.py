from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

User = get_user_model()
class LoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('account_login')
        self.username = 'testuser'
        self.password = 'admin211221'
        self.user = User.objects.create_user(
            self.username, email='testuser@example.com', password=self.password)
        EmailAddress.objects.create(user=self.user, email=self.user.email, primary=True, verified=True)

    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        # Make sure login fails with wrong credentials
        response = self.client.post(self.login_url, {'login': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        # Make sure login succeeds with correct credentials
        response = self.client.post(self.login_url, {'login': self.username, 'password': self.password})
        self.assertRedirects(response, reverse('home'))
        # Make sure user is authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)