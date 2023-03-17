from django.contrib import admin
from django.urls import path, include
from apps.user.api.verify_account import VerifyOTPAPIView
from apps.user.api.singup import UserSignUpAPIView

urlpatterns = [
    path('user/registration/', UserSignUpAPIView.as_view()),
    path('user/verify/', VerifyOTPAPIView.as_view())
]
