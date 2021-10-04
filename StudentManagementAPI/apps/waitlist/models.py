from django.db import models

from apps.utils.models import Timestamps


class WaitlistEntry(Timestamps, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_name = models.EmailField(verbose_name='email adress', max_length=255, unique=True)
    notes = models.TextField()
