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

    def test_post_update(self):
        response = self.client.get('/post/1/edit/')
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 403)


    def test_Post_post_Update(self):
        response = self.client.post(reverse('edit_post', args='1'),
        {
            'title':'Update',
            'body': 'New body'
        })
        # self.assertContains(response, 'Update')
        self.assertNotEqual(response.status_code, 302)
        self.assertEqual(response.status_code, 403)


# permissions issue
    def test_post_delete(self):
        response = self.client.get('/post/1/delete/')
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 403)

    # permissions issue 
    # def test_POST_delete(self):
    #     post_response = self.client.post(reverse('delete_post',args='1'))
    #     self.assertEqual(post_response.status_code, 302)


class SignUptest(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup(self):
        newuser = get_user_model().objects.create_user(
        self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
