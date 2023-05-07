# Django
from django.urls import path

# Project
from apps.main.branch.api import BranchCreateAPIView


urlpatterns = [
    path('create/', BranchCreateAPIView.as_view()),
]
