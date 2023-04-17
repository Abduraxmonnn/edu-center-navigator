# Django
from django.urls import path, include

# Rest-Framework
from rest_framework import routers

# Project
from apps.main.center.api import CenterCreateAPIView, CenterListViewSet

router = routers.DefaultRouter()
router.register(r'list', CenterListViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('create/', CenterCreateAPIView.as_view()),
]
