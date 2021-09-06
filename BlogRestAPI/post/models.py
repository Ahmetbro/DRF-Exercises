from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import rest_framework

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    title = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    draft = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='profiles/%Y/%m/')
    #modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='modifiedbyuser')

    def get_slug(self):
        slug = slugify(self.title.replace("ı","i"))
        unique = slug
        number = 1
        
        while Post.objects.filter(slug=unique).exists():
            unique = f'{slug}-{number}'
            number +=1

        return unique

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user)


