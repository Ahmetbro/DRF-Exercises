import re
from django.contrib.auth.models import User
from django.http import response
from rest_framework.test import APITestCase
from django.urls import reverse
import json
from post.models import Post


class PostCreate(APITestCase):  # title, user req
    login_url = reverse("token_obtain_pair")
    def setUp(self):
        self.url = reverse("post:posts")
        self.username = "ahmet1234"
        self.password = "sifre1234"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.test_jwt_authentication()
    
    def test_jwt_authentication(self):
        response = self.client.post(self.login_url, data = {"username":"ahmet1234", "password":"sifre1234"})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ self.token)

    # create post test
    def test_create_post(self):
        data = {
            "title": "posst title"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)
    
    # list posts test
    def test_list_post(self):
        response = self.client.get(self.url)
        #self.assertEqual(200, response.status_code)
        self.assertTrue(len(json.loads(response.content)["results"]) == Post.objects.all().count())

    # test unauthorizzed user post
    def test_unauthorized_post(self):
        self.client.credentials()
        data = {
            "title": "posst title"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(401, response.status_code)
        response2 = self.client.get(self.url)
        self.assertEqual(401, response2.status_code)

class PostDetailDelete(APITestCase):
    login_url = reverse("token_obtain_pair")
    def setUp(self):
        self.username = "ahmet1234"
        self.password = "sifre1234"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user2 = User.objects.create_user(username='Ahmet57', password=self.password)
        self.post = Post.objects.create(title='new post')
        self.url = reverse("post:post-detail", kwargs={'slug': self.post.slug})
        self.test_jwt_authentication()
    
    def test_jwt_authentication(self, username = "ahmet1234", password="sifre1234"):
        response = self.client.post(self.login_url, data={"username": username, "password": password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
    
    # delete post
    def test_post_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)
        self.assertFalse(Post.objects.filter(slug=self.post.slug).exists())

    # delete unowned post
    def test_delete_other_user(self):
        self.test_jwt_authentication("Ahmet57")
        response = self.client.delete(self.url)
        self.assertEqual(403, response.status_code)
    
    # update post
    def test_update_post(self):
        response = self.client.put(self.url, data={'title':'title2'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(Post.objects.get(id=self.post.id).title, "title2")

        # update post w diffrent user
    def test_update_post_different_user(self):
        self.test_jwt_authentication("Ahmet57")
        response = self.client.put(self.url, data={'title':'titleee2'})
        self.assertEqual(403, response.status_code)
        self.assertNotEqual(Post.objects.get(id=self.post.id).title, "titleee2")

    # test unauthorized user get
    def test_unauthorized_user(self):
        self.client.credentials()
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)
