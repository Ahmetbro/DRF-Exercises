from apps.utils.models import Timestamps
from django.db.models.fields import CharField
from apps.users.models import MyUser
from django.db import models
from django.utils.text import slugify

class List(Timestamps, models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='Users')
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name


class ListItem(Timestamps, models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')
    text = models.TextField()
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.slug