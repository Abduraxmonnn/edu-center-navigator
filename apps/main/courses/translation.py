# Django
from modeltranslation.translator import TranslationOptions, register

# Project
from apps.main.courses.models import CourseCategory, Course


@register(CourseCategory)
class CourseCategoryTranslationOption(TranslationOptions):
    fields = ('name', )


@register(Course)
class CourseTranslationOption(TranslationOptions):
    fields = ('name', )
