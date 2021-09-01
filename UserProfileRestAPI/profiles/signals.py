from django.contrib.auth.models import User
from profiles.models import Profile, ProfilStatus
from django.db.models.signals import post_save
from django.dispatch import receiver



#### Create User profile after creating new user 
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=Profile) 
def create_profile_status(sender, instance, created, **kwargs):
    if created:
        ProfilStatus.objects.create(
            user_profile = instance,
            status_message = f'{instance.user.username} joined just now!'
            )