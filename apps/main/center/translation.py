# Django
from modeltranslation.translator import TranslationOptions, register

# Project
from apps.main.center.models import Center


@register(Center)
class CenterTranslationOption(TranslationOptions):
    fields = ('name', )
