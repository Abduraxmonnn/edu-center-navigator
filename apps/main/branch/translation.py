# Django
from modeltranslation.translator import TranslationOptions, register

# Project
from apps.main.branch.models import Branch


@register(Branch)
class BranchTranslationOption(TranslationOptions):
    fields = ('name', )
