# Django
from django.contrib import admin

# Project
from apps.address.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'district', 'street', 'lat', 'lng', 'created_date', 'last_updated']
    list_display_links = ['id', 'district', 'street']
    list_filter = ['district', 'street', 'created_date']
    list_editable = ['lat', 'lng']
