# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework.viewsets import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter


# Project
from apps.main.courses.models import Course
from apps.main.courses.serializers import CourseSerializer
from apps.custom_filters import CoursesFilter

class CourseListViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CoursesFilter
    search_fields = [
        '^name',
        'category__name',
        'price',
        'course_duration',
    ]
    ordering_fields = ['price', 'course_duration', '-id']
    ordering = ['-id']
