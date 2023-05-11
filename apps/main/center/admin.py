# Django
from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

# Project
from apps.main.center.models import Center


@admin.register(Center)
class CenterAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'main_course', 'is_public', 'score', 'number_students']
    list_display_links = ['name', 'main_course']
    list_filter = ['name', 'main_course', 'is_public', 'number_students']
    # readonly_fields = ['get_image']

    # def get_image(self, obj):
        # return format_html('<img src="{0}" width="auto" height="150px" />'.format(obj.image.url))

    # get_image.short_description = 'Image'
