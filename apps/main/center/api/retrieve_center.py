# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

# Project
from apps.main.center.models import Center
from apps.main.center.serializers import CenterRetrieveSerializer


class CenterRetrieveViewSet(viewsets.GenericViewSet,
                        mixins.RetrieveModelMixin):
    queryset = Center.objects.all()
    serializer_class = CenterRetrieveSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
