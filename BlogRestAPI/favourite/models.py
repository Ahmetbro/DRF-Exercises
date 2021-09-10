from django.db import models
from django.contrib.auth.models import User
from post.models import Post
# Create your models here.

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favpost')
    content = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username