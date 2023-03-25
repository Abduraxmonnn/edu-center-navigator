# Rest-Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

# Project
from apps.user.models import User
from apps.user.serializers import UserSerializer


class UserListView(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
