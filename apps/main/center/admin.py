# Django
from django.contrib import admin
from django.utils.html import mark_safe

# Project
from apps.main.center.models import Center


@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'name', 'main_course', 'is_public', 'score']
    list_display_links = ['name', 'main_course']
    list_filter = ['name', 'main_course', 'is_public']
    readonly_fields = ['get_image']

    def get_image(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % self.image)

    get_image.short_description = 'Image'
