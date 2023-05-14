# Django
from django.urls import path

# Project
from apps.user.api import UserSignUpAPIView, UserLogInView, VerifyOTPAPIView, UserTokenAPIView, UserMeView, UserListView, \
    UserDeleteAPIView

urlpatterns = [
    path('signup/', UserSignUpAPIView.as_view()),
    path('signin/', UserLogInView.as_view()),
    path('verify/', VerifyOTPAPIView.as_view()),
    path('token/get/<int:pk>/', UserTokenAPIView.as_view()),
    path('me/<int:pk>/', UserMeView.as_view()),
    path('list/', UserListView.as_view({'get': 'list'})),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view()),
]
