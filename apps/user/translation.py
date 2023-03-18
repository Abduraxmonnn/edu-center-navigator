# Django
from modeltranslation.translator import TranslationOptions, register

# Project
from apps.user.models import User


@register(User)
class UserTranslationOption(TranslationOptions):
    fields = ('name', 'surname')
