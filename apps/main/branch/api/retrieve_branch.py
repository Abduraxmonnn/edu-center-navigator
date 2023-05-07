# Rest-Framework
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

# Project
from apps.main.branch.models import Branch
from apps.main.branch.serializers import BranchRetrieveSerializer


class BranchRetrieveViewSet(viewsets.GenericViewSet,
                            mixins.RetrieveModelMixin):
    queryset = Branch.objects.all()
    serializer_class = BranchRetrieveSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
