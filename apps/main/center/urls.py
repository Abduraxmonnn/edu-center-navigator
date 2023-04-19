# Django
from django.urls import path, include

# Rest-Framework
from rest_framework import routers

# Project
from apps.main.center.api import CenterCreateAPIView, CenterListViewSet, CenterUpdateViewSet

router = routers.DefaultRouter()
router.register(r'list', CenterListViewSet)
# router.register(r'update/<int:pk>/', CenterUpdateViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('create/', CenterCreateAPIView.as_view()),
    path('update/<int:pk>/', CenterUpdateViewSet.as_view({'put': 'update'})),
]
