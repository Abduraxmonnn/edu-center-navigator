# Django
from modeltranslation.translator import TranslationOptions, register

# Project
from apps.main.address.models import Address


@register(Address)
class AddressTranslationOption(TranslationOptions):
    fields = ('district', 'street', 'apartment_letter')
