# Django
from django.contrib import admin
from django.utils.html import mark_safe, format_html
from modeltranslation.admin import TranslationAdmin

# Project
from apps.main.teacher.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(TranslationAdmin):
    list_display = ['image', 'name', 'experience_year']
    list_display_links = ['name', 'experience_year']
    list_filter = ['name']

    # def get_image(self, obj):
    #     return format_html('<img src="{0}" width="auto" height="150px" />'.format(obj.image.url))

    # get_image.short_description = 'Image'
