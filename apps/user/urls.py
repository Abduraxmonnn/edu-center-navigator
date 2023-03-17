# Django
from django.urls import path

# Project
from apps.user.api import UserSignUpAPIView, VerifyOTPAPIView, UserTokenAPIView

urlpatterns = [
    path(r'signup/', UserSignUpAPIView.as_view()),
    path(r'verify/', VerifyOTPAPIView.as_view()),
    path(r'token/get/<int:pk>/', UserTokenAPIView.as_view())
]
