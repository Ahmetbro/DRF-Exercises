from apps.lectures.models import Lecture
from django.contrib import admin


class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer_name', 'date')
    search_fields = ('title', 'lecturer_name')

admin.site.register(Lecture, LectureAdmin)