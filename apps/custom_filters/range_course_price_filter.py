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
