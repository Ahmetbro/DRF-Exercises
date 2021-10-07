from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email adress', unique=True, max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True, related_name='userprofile')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    fb_profile = models.CharField(max_length=150)
    twitter_profile =models.CharField(max_length=150)
    linkedin_profile = models.CharField(max_length=150)
    website = models.CharField(max_length=150)

@receiver(post_save, sender=MyUser)
def create_userprofile(sender, instance, created, **kwargs):
    if not created:
        return
    UserProfile.objects.create(user=instance)
    instance.userprofile.save()
    
