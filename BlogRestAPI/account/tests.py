from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import response, status
from rest_framework.test import APITestCase
from django.urls import reverse
import json


# doğru verilerle kayıt işlemi yap
# şifre invalid olabilir
# kullanıcı adı daha önce alınmış olabilir
# üye girişi yaptıysak sayfa gözükmemeli
# token ile giriş yapılırsa 403 hatası
class UserRegistration(APITestCase):
    url = reverse("account:register") # url.py daki appname:pathname
    url_login = reverse("token_obtain_pair")
    def test_user_registration(self):
        """Doğru veriler ile kayıt işlemi"""

        data = {
            "username" : "ahmetttest",
            "password" : "denemedee1231",
        }

        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_user_invalid_pw(self):
        """Invalid password ile kayıt işlemi"""

        data = {
            "username" : "ahmetttest",
            "password" : "1",
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_unique_name(self):
        """unique username ile kayıt işlemi"""
        self.test_user_registration()
        data = {
            "username" : "ahmetttest",
            "password" : "asdas123123",
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_user_authenticated_registration(self):
        """session ile giriş yapmış kullanıcı sayfayı görememelii"""
        self.test_user_registration()
        
        self.client.login(username = "ahmetttest", password = "denemedee1231")
        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)

    def test_user_authenticated_token_registration(self):
        """token ile giriş yapmış kullanıcı sayfayı görememelii"""
        self.test_user_registration()
        data = {
            "username" : "ahmetttest",
            "password" : "denemedee1231",
        }
        
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)

        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer '+ token)
        
        response2 = self.client.get(self.url)
        self.assertEqual(403, response2.status_code)


class UserLogin(APITestCase):
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "ahmet"
        self.passsword = "sifre123"
        self.user = User.objects.create_user(username = self.username, password = self.passsword)

    def test_user_token(self):
        response = self.client.post(self.url_login, {"username":"ahmet", "password": "sifre123"})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))
    
    def test_user_invalid_data(self):
        response = self.client.post(self.url_login, {"username":"ahrteemet", "password": "siffretre123"})
        self.assertEqual(401, response.status_code)

    def test_user_empty_data(self):
        response = self.client.post(self.url_login, {"username":"", "password": ""})
        self.assertEqual(400, response.status_code)


class UserPasswordChange(APITestCase):
    url = reverse("account:change-password")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "ahmet"
        self.passsword = "sifre123"
        self.user = User.objects.create_user(username = self.username, password = self.passsword)

    def login_with_token(self):
        data = {
            "username" : "ahmet",
            "password" : "sifre123"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_is_authenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)

    def test_with_valid_informations(self):
        self.login_with_token()
        data = {
            "old_password": "sifre123",
            "new_password": "asdad123qw23"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(204, response.status_code)
    
    def test_with_wrong_informations(self):
        self.login_with_token()
        data = {
            "old_password": "sadasaaaa",
            "new_password": "asdad123qw23"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(400, response.status_code)
    
    def test_with_empty_informations(self):
        self.login_with_token()
        data = {
            "old_password": "",
            "new_password": ""
        }
        response = self.client.put(self.url, data)
        self.assertEqual(400, response.status_code)
    

class UserProfileUpdate(APITestCase):
    url = reverse("account:me")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "ahmet"
        self.passsword = "sifre123"
        self.user = User.objects.create_user(username = self.username, password = self.passsword)

    def login_with_token(self):
        data = {
            "username" : "ahmet",
            "password" : "sifre123"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_is_authenticated_user(self): # oturum açılmadan update sayfası acılırsa
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)
    
     # valid informations
    def test_with_valid_informations(self):
        self.login_with_token()
        data = {
            "id" : 1,
            "first_name": "",
            "last_name": "",
            "profile": {
                "id": 1,
                "note": "",
                "twitter": "asdas"
            }
        }

        response = self.client.put(self.url, data, format = 'json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content), data)