from apps.users.models import MyUser
from apps.utils.models import Timestamps
from django.db import models

class Task(Timestamps, models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255) 
    description = models.TextField(blank=True,null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    text = models.CharField(choices={(('R'),('Urgent')),(('G'),('Not Urgent'))}, max_length=100)
    task = models.ManyToManyField(Task)