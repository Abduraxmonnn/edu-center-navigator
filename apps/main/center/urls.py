# Django
from django.urls import path, include

# Rest-Framework
from rest_framework import routers

# Project
from apps.main.center.api import CenterCreateAPIView, CenterListViewSet, CenterUpdateViewSet, DeleteCenterAPIView, \
    CenterRetrieveViewSet, CenterCoursesListViewSet

router = routers.DefaultRouter()
router.register(r'list', CenterListViewSet)
router.register(r'list_courses', CenterCoursesListViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('create/', CenterCreateAPIView.as_view()),
    path('update/<int:pk>/', CenterUpdateViewSet.as_view({'put': 'update'})),
    path('delete/<int:pk>/', DeleteCenterAPIView.as_view()),
    path('retrieve/<int:pk>/', CenterRetrieveViewSet.as_view({'get': 'retrieve'}))
]
