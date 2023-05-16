from django_filters import FilterSet, RangeFilter
from django_filters import rest_framework as filters

from apps.main.center.models import Center
from apps.main.courses.models import Course


class CoursesFilter(FilterSet):
    price = RangeFilter()

    class Meta:
        model = Course
        fields = [
            'category__name',
            'name',
            'price',
            'course_duration'
        ]

class CenterFilter(FilterSet):
    courses__price = RangeFilter()

    class Meta:
        model = Center
        fields = [
            'name',
            'main_course__name',
            'courses__name',
            'courses__course_duration',

            'center_address__district',
            'courses__price',
        ]
