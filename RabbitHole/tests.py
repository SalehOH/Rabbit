from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Room, Post, Reply, Like
from RabbitHole.forms import PostForm,ReplyForm,RoomForm

User = get_user_model()

#views tests

class RoomViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpass'
        )
        self.room = Room.objects.create(
            name='testroom', avatar='room-avatar.jpg', creator=self.user
        )
        self.post = Post.objects.create(
            content='test post content', room=self.room, user=self.user
        )
        self.reply = Reply.objects.create(
            content='test reply content', post=self.post, user=self.user
        )


    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'RabbitHole/index.html')


    def test_room_view(self):
        response = self.client.get(reverse(('room'), args=[self.room.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'RabbitHole/room.html')
        #self.assertContains(response, self.post.content)
        #self.assertContains(response, self.reply.content)

    def test_create_room_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create_room'), {'name': 'testroom'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Room.objects.filter(name='testroom').exists())



    def test_join_room_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('join_room', args=[self.room.name, self.user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.room.participants.all().count(), 1)

    def test_create_post_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create_post', args=[self.room.name]), {'content': 'test post content'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Post.objects.filter(content='test post content').exists())

    def test_create_reply_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create_reply', args=[self.room.name, self.post.id, self.post.slug]), {'content': 'test reply content'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Reply.objects.filter(content='test reply content').exists())

    def test_like_post_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('like_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], True)
        self.assertEqual(response.json()['likes'], 1)


    def test_dislike_post_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('dislike_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], False)
        self.assertEqual(response.json()['likes'], -1)
        

class PostTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.room = Room.objects.create(name='Test Room', avatar=SimpleUploadedFile("room_avatar.png", b"file_content"), creator=self.user)
        self.post = Post.objects.create(content='Test Post', room=self.room, user=self.user)

    def test_post_creation(self):
        self.assertEqual(str(self.post), 'Test Post')
        self.assertEqual(Post.objects.count(), 1)

    def test_post_slug_creation(self):
        self.assertEqual(self.post.slug, '')
        self.assertEqual(Post.objects.get(pk=self.post.pk).slug, '')


class ReplyTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.room = Room.objects.create(name='Test Room', avatar=SimpleUploadedFile("room_avatar.png", b"file_content"), creator=self.user)
        self.post = Post.objects.create(content='Test Post', room=self.room, user=self.user)
        self.reply = Reply.objects.create(content='Test Reply', post=self.post, user=self.user)

    def test_reply_creation(self):
        self.assertEqual(str(self.reply), 'Test Reply')
        self.assertEqual(Reply.objects.count(), 1)

    def test_reply_slug_creation(self):
        self.assertEqual(self.reply.slug, 'test-reply')
        self.assertEqual(Reply.objects.get(pk=self.reply.pk).slug, 'test-reply')


class RoomTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.room = Room.objects.create(name='testroom', avatar='room.jpg', creator=self.user)

    def test_room_str(self):
        room_str = str(self.room)
        expected_str = 'testroom'
        self.assertEqual(room_str, expected_str)
        
    def test_room_creator(self):
        creator = self.room.creator
        self.assertEqual(creator, self.user)
        

#fourms test#



class RoomFormTest(TestCase):
    def test_form(self):
        data = {
            'name': 'test name',
                'avatar': 'default.png'}
        
        form = RoomForm(data=data)
        self.assertTrue(form.is_valid())

    


class PostFormTest(TestCase):
    def post_form_Test(self):
        data = {'title': 'Test Post', 'content': 'test post', 'image': 'test_image.jpg'}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    


class ReplyFormTest(TestCase):
    def test_valid_form(self):
        data = {'title': 'Test Reply', 'content': 'This is a test reply', 'image': 'test_image.jpg'}
        form = ReplyForm(data=data)
        self.assertTrue(form.is_valid())


    
#urltest

class TestUrls(TestCase):

    def test_home_url(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_url(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_page_url(self):
        url = reverse('user_page', args=['testuser'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_room_url(self):
        url = reverse('create_room')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_room_url(self):
        url = reverse('room', args=['testroom'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_join_room_url(self):
        url = reverse('join_room', args=['testroom', '123'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        
    
    def test_create_post_url(self):
        url = reverse('create_post', args=['testpost'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        
    def test_post_url(self):
        url = reverse('post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_create_reply_url(self):
        url = reverse('create_reply',args=['testreply'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
       
        
    
    def test_delete_post_url(self):
        url = reverse('delete_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_delete_reply_url(self):
        url = reverse('delete_reply')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_like_post_url(self):
        url = reverse('like_post', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_dislike_post_url(self):
        url = reverse('dislike_post', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_like_reply_url(self):
        url = reverse('like_reply', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_dislike_reply_url(self):
        url = reverse('dislike_reply', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)