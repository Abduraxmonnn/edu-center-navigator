# Python
import datetime

# Django
from django.utils import timezone

# Rest-Framework
from rest_framework import status
from rest_framework.views import APIView, Response

# Project
from apps.user.models import User
from apps.user.serializers.verify_account import VerifyOtpSerializer


class VerifyOTPAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyOtpSerializer(data=data)

            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email__iexact=email)
                if user.exists():
                    if user.first().is_verified is True:
                        return Response({
                            "message": "User exists",
                            'data': serializer.errors
                        }, status=status.HTTP_400_BAD_REQUEST)

                first_user = user.first()
                if not first_user.otp == otp:
                    return Response({
                        'message': 'OTP is wrong',
                        'data': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)

                user_ex_time = first_user.expires_at + datetime.timedelta(minutes=5)
                expires_check_time = user_ex_time <= timezone.now()
                if expires_check_time is False:
                    return Response({
                        'message': 'Verified code has expired',
                        'data': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)

                first_user.is_verified = True
                first_user.save()

                return Response({
                    'message': 'Account is verified',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                'message': 'Something went wrong',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as ex:
            print(ex)
            return ex
