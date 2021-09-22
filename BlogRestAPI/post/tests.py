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