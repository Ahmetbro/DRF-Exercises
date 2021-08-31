from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='profiles/%Y/%m/')

    def __str__(self):
        return self.user.username

    def save(self, force_insert=False, *args, **kwargs):             ## overwriting save method for image size,
        ## image resize                                              ## force_insert=false yaptım çünkü user oluştuduğumda sinyal ile prifli de oluştururken 
        super().save(*args, *kwargs)                                 ## 'Cannot force both insert and updating in model saving' hatası aldım
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.photo.path)

    # class Meta:
    #     verbose_name_plural = 'Profiller' django admin sitesinddeki model adı

class ProfilStatus(models.Model):
    user_profile = ForeignKey(Profile, on_delete=models.CASCADE)
    status_message = models.CharField(max_length=240)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Profile Status'

    def __str__(self):
        return str(self.user_profile)