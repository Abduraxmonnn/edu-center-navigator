# Rest-Framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.user.models import User
from apps.user.serializers.user import UserDeleteSerializer


class UserDeleteAPIView(APIView):
    """
    This API used for Delete Centers.
    This api get an ID of Center
    """
    model = User
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer

    def delete(self, request, pk=None):
        try:
            obj = User.objects.get(pk=pk)
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

