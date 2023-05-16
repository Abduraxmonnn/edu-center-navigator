# Django
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# Project
from apps.main.courses.api import CourseListViewSet

router = DefaultRouter()
# router.register('create', TeacherCreateViewSet, 'teacher_create')
router.register('list/range/filter', CourseListViewSet, 'course_list')
# router.register('retrieve', TeacherRetrieveViewSet, 'teacher_retrieve')
# router.register('update', TeacherUpdateViewSet, 'teacher_update')
# router.register('destroy', TeacherDestroyViewSet, 'teacher_destroy')

urlpatterns = [
    path('', include(router.urls))
]
