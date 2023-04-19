# Rest-Framework
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.center.models import Center
from apps.main.center.serializers import CenterUpdateSerializer


class CenterUpdateViewSet(ModelViewSet):
    queryset = Center.objects.all()
    serializer_class = CenterUpdateSerializer
