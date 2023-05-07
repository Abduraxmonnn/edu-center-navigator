# Django
from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

# Project
from apps.main.branch.models import Branch


@admin.register(Branch)
class BranchAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'center_name', 'is_public', 'visited']
    list_display_links = ['name', 'center_name']
    list_filter = ['name', 'is_public']
    # readonly_fields = ['get_image']

    def center_name(self, obj):
        return obj.center.name

    # def get_image(self, obj):
        # return format_html('<img src="{0}" width="auto" height="150px" />'.format(obj.image.url))

    # get_image.short_description = 'Image'
