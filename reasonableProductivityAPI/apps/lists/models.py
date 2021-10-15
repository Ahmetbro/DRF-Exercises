from apps.utils.models import Timestamps
from django.db.models.fields import CharField
from apps.users.models import MyUser
from django.db import models
from django.db.models.fields.related import ForeignKey

class List(Timestamps, models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='Users')
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.user
