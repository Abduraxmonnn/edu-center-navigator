# Django
from django.contrib.auth import authenticate, login
from django.db.models import ProtectedError

# Rest-Framework
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import APIView
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Project
from apps.user.serializers.user import UserSerializer
from apps.user.models import User


class UserMeView(APIView):
    def get(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response({
            'status_code': 200,
            'message': 'Successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
