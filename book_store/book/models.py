from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    book = models.CharField(max_length=120)
    author = models.CharField(max_length=100)
    info = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField()

    def __str__(self):
        return f'{self.book} - {self.author}'


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments') # db de oluşturulan kitapları seçip o kitaba yorum atmamızı sağlar.
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name') # giriş yapılan user name i comment_owner olarak atar.
    comment = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    
    def __str__(self):
        return str(self.rating)