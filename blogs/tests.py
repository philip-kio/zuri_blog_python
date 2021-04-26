from django.http import response
from django.test import TestCase
from .models import post
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.


class BlogTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password= 'testeruser'
        )


        self.post = post.objects.create(
            title = 'Test',
            body = 'This test of ours.',
            author = self.user
        )


    def test_str(self):
        post1 = post(title= 'Test')
        self.assertEqual(str(post1), self.post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}','This test of ours.')

    def test_post_listView(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'This test of ours.')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detailView(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100/')
        self.assertEqual(no_response.status_code,404)
        self.assertEqual(response.status_code,200)