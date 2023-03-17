# Rest-Framework
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# Project
from apps.user.models import User


class UserTokenAPIView(APIView):
    def get(self, request, pk=None):
        user = User.objects.filter(pk=pk)
        if not user.exists():
            return Response({
                "error_message": "User does not Exist"
            })
        user = user.first()
        token = Token.objects.get(user_id=user.id)
        return Response({
            "token": token.key
        }, status=status.HTTP_200_OK)
