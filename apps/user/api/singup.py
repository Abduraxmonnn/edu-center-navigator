# Rest-Framework
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.utils import timezone

# Project
from apps.user.models import User
from apps.user.serializers.singup import UserSignUpSerializer
from apps.emails.verify_account.send_email import send_otp_via_email


class UserSignUpAPIView(APIView):
    model = User
    queryset = User.objects.order_by('-id').all()
    serializer_class = UserSignUpSerializer

    def post(self, request):
        try:
            serializer = UserSignUpSerializer(data=request.data, context={'request': request})

            if serializer.is_valid():
                name = serializer.validated_data['name']
                surname = serializer.validated_data['surname']
                username = serializer.validated_data['username']
                dob = serializer.validated_data['dob']
                phone_number = serializer.validated_data['phone_number']
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']

                check_user = User.objects.filter(email__iexact=email)
                if check_user.exists():
                    if check_user.first().is_verified is True:
                        return Response({
                            "message": "User exists",
                        }, status=status.HTTP_400_BAD_REQUEST)

                if check_user.exists():
                    if check_user.first().is_verified is False:
                        user = User.objects.create_user(email=email, password=password)
                        user.name = name
                        user.surname = surname
                        user.username = username
                        user.dob = dob
                        user.phone_number = phone_number
                        user.is_verified = False
                        user.expires_at = timezone.now()
                        user.save()

                        token = Token.objects.create(user=user)
                        send_otp_via_email(user.email)

                        return Response({
                            'message': 'Registration successfully check email',
                            'token': token.key,
                            'data': serializer.data
                        }, status=status.HTTP_200_OK)

            return Response({
                'message': 'Something went wrong',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            return ex
