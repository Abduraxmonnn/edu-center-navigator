# Django
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

# Project
from apps.main.comments.models import CommentHelper, Comment


class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(CommentHelper)
class CommentHelperAdmin(TranslationAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = ['owner', 'text', 'is_updated', 'created_date', 'last_updated']
    list_display_links = ('owner',)
    list_filter = ['created_date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_helper', 'is_updated', 'created_date', 'last_updated')
    list_display_links = ('comment_helper', )
    list_filter = ('created_date', )
