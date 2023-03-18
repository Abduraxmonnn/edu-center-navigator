# Django
from django.contrib import admin
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin

# Project
from apps.main.teacher.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(TranslationAdmin):
    list_display = ['get_image', 'name', 'experience_year']
    list_display_links = ['name', 'experience_year']
    list_filter = ['name']

    def get_image(self, image):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % image)

    get_image.short_description = 'Image'
