# Django
from django.contrib import admin
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin

# Project
from apps.main.center.models import Center


@admin.register(Center)
class CenterAdmin(TranslationAdmin):
    list_display = ['get_image', 'name', 'main_course', 'is_public', 'score']
    list_display_links = ['name', 'main_course']
    list_filter = ['name', 'main_course', 'is_public']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return format_html('<img src="{0}" width="auto" height="150px" />'.format(obj.image.url))

    get_image.short_description = 'Image'
