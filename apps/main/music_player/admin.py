# Django
from django.contrib import admin

# Project
from apps.main.music_player.models import Music


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['name', 'file']
