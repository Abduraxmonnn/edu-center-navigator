# Django
from modeltranslation.translator import TranslationOptions, register

# Project
from apps.main.comments.models import CommentHelper


@register(CommentHelper)
class CommentHelperTranslationOption(TranslationOptions):
    fields = ('text', )
