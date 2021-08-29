from book.models import Book
import os
import random

from rest_framework import serializers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_store.settings')

import django
django.setup()
### Modellerimize ve django içeriklerine erişmek için yukarıdaki gibi ayarlamaları yapmamız lazım
### SIRALAMA ÇOK ÖNEMLİ

from django.contrib.auth.models import User
from faker import Faker
import requests
from prettyprinter import pprint
from book.serializers import BookSerializer

def set_user():
    fake = Faker(['en_US'])

    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'
    
    user_check = User.objects.filter(username = u_name)

    while user_check.exists():
        fake = Faker(['en_US'])
        u_name = u_name + str(random.randrange(1,99))
        user_check = User.objects.filter(username = u_name)


    user = User(
        username= u_name,
        first_name= f_name,
        last_name= l_name,
        email= email,
        is_staff = fake.boolean(chance_of_getting_true=40),
    )

    user.set_password('testing321..')
    user.save()

def set_book(topic):
    
    fake = Faker(['en_US'])
    url = 'http://openlibrary.org/search.json'
    payload = {'q':topic}
    response = requests.get(url, params=payload)
    if response.status_code != 200:
        print('request unidentified', requests.status_codes)
        return
    json = response.json()
    books= json.get('docs')
    for buk in books:
        data = dict(
        book = buk.get('title'),
        author = buk.get('author_name')[0],
        info = '-'.join(buk.get('text')),
        publish_date = fake.date_time_between(start_date='-30y', end_date='now', tzinfo=None),
        )
    
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(data['book'], 'kaydedildi')
        else:
            continue