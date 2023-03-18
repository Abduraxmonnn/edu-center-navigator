# Django
from modeltranslation.translator import TranslationOptions, register

# Project
from apps.main.teacher.models import Teacher


@register(Teacher)
class TeacherTranslationOption(TranslationOptions):
    fields = ('name', 'description')
