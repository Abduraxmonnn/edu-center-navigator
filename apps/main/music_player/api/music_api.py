# Rest-Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser

# Project
from apps.main.music_player.serializers import MusicSerializer
from apps.main.music_player.models import Music
from apps.permissions.specific_user import AdminUserPermission


class MusicCreateViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']


class MusicListViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']


class MusicRetrieveViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']


class MusicUpdateViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['put']


class MusicDestroyViewSet(ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [AdminUserPermission]
    http_method_names = ['delete']
