# Django
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

# Project
from apps.main.address.models import Address


@admin.register(Address)
class AddressAdmin(TranslationAdmin):
    list_display = ['id', 'district', 'street', 'lat', 'lng', 'created_date', 'last_updated']
    list_display_links = ['id', 'district', 'street']
    list_filter = ['district', 'street', 'created_date']
    list_editable = ['lat', 'lng']
