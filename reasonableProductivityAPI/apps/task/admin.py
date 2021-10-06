from django.db import models
from apps.task.models import Task
from django.contrib import admin

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')

admin.site.register(Task, TaskAdmin)