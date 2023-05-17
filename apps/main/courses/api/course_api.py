# Django
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

# Rest-Framework
from rest_framework.viewsets import mixins
from rest_framework import viewsets, views, status
from rest_framework.permissions import AllowAny
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

class CourseCenterListAPIView(views.APIView):
    filter_backends = (filters.DjangoFilterBackend,)

    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.
        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        result = []
        query = Course.objects.all()
        filtered_qs = self.filter_queryset(query)
        for item in filtered_qs:
            result.append({
                'center_id': item.center_set.values('id'),
                'center_name': item.center_set.values('name'),
                'course_name': item.name,
                'course_price': item.price,
                'course_duration': item.course_duration
            })
        return Response({
            "status_code": 200,
            "data": result,
        }, status=status.HTTP_200_OK)
