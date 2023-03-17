# Django
from django.contrib import admin
from django.utils.html import mark_safe

# Project
from apps.main.teacher.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'name', 'experience_year']
    list_display_links = ['name', 'experience_year']
    list_filter = ['name']

    def get_image(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % self.image)

    get_image.short_description = 'Image'
