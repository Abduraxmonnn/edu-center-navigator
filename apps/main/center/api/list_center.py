# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.main.center.models import Center
from apps.main.center.serializers import CenterListSerializer, CenterCoursesListSerializer
from apps.custom_filters import CenterFilter

class CenterListViewSet(ModelViewSet):
    queryset = Center.objects.filter(is_public=True)\
        .select_related('center_address', 'main_course')\
        .prefetch_related('courses', 'top_teachers')
    serializer_class = CenterListSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CenterFilter
    search_fields = [
        '^name',
        'main_course__name',
        'courses__category__name',
        'courses__name',

        'center_address__district',
    ]
    ordering_fields = ['name', 'main_course__name', '-id']
    ordering = ['-id']


class CenterCoursesListViewSet(ModelViewSet):
    queryset = Center.objects.filter(is_public=True).prefetch_related('courses', 'courses__category')
    serializer_class = CenterCoursesListSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CenterFilter
    search_fields = [
        '^name',
        'main_course__name',
        'courses__name',

        'center_address__district',
    ]
    ordering_fields = ['name', 'main_course__name', '-id', 'price']
    ordering = ['-id']
