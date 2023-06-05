# Django
from django.contrib import admin
from rangefilter.filters import DateRangeFilterBuilder

# Project
from apps.main.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'email_from', 'created_date')
    list_display_links = ('subject', )
    list_filter = (("created_date", DateRangeFilterBuilder()), )
    ordering = ('-id', )
