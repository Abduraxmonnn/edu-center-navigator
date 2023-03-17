# Django
from django.contrib import admin

# Project
from apps.main.courses.models import CourseCategory, Course


class CourseInline(admin.TabularInline):
    model = Course


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    inlines = [
        CourseInline
    ]
    list_display = ['name', 'created_date', 'last_updated']
    list_display_links = ('name',)
    list_filter = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'get_categories', 'price', 'course_duration']
    list_display_links = ('name', 'category')
    list_filter = ['category', 'price']

    def get_categories(self, obj):
        return ' | '.join([c.name for c in obj.coursecategory.all().only('name')])
