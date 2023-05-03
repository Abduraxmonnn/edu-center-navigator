# Django
from django.shortcuts import get_object_or_404

# Rest-Framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.center.models import Center
from apps.main.center.serializers import CenterDeleteSerializer


class DeleteCenterAPIView(APIView):
    """
    This API used for Delete Centers.
    This api get an ID of Center
    """
    model = Center
    queryset = Center.objects.all()
    serializer_class = CenterDeleteSerializer

    def delete(self, request, pk=None):
        try:
            obj = Center.objects.get_object_or_404(pk=pk)
            obj.delete()
        except Exception as ex:
            return Response({
                'status_code: ': 400,
                'message: ': f'Object does not exists or {ex}'
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status_code: ': 200,
            'message: ': 'Object deleted successfully'
        }, status=status.HTTP_200_OK)

