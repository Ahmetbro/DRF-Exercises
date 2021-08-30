from django.contrib.auth.models import User
from profiles.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver



#### Create User profile after creating new user 
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)