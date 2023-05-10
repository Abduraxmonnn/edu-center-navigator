# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.main.branch.models import Branch
from apps.main.branch.serializers import BranchListSerializer


class BranchListViewSet(ModelViewSet):
    queryset = Branch.objects.filter(is_public=True)\
        .select_related('branch_address')\
        .prefetch_related('courses')
    serializer_class = BranchListSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'name',
        'courses__name',
        'courses__course_duration',

        'branch_address__district',
    ]
    search_fields = [
        'name',
        'courses__name',

        'branch_address__district',
    ]
    ordering_fields = ['name', '-id']
    ordering = ['-id']
