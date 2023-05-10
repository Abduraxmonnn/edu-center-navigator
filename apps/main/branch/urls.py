# Django
from django.urls import path

# Project
from apps.main.branch.api import BranchCreateAPIView, BranchListViewSet, BranchRetrieveViewSet


urlpatterns = [
    path('create/', BranchCreateAPIView.as_view()),
    path('list/', BranchListViewSet.as_view({'get': 'list'})),
    path('retrieve/<int:pk>/', BranchRetrieveViewSet.as_view({'get': 'retrieve'}))
]
