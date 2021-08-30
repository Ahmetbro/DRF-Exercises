from django.contrib import admin
from profiles.models import ProfilStatus, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(ProfilStatus)