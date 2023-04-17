# Django
from django.utils import timezone

# Rest-Framework
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# Project
from apps.user.models import User
from apps.user.serializers.user import UserSignUpSerializer
from apps.emails.send_email_via.send_email import send_otp_via_email


class UserSignUpAPIView(APIView):
    model = User
    queryset = User.objects.order_by('-id').all()
    serializer_class = UserSignUpSerializer

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

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
                    "status_code": 400,
                    "message": "User exists",
                }, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(email=email, password=password)
        user.name = name
        user.surname = surname
        user.username = username
        user.password = password
        user.dob = dob
        user.phone_number = phone_number
        user.is_verified = False
        user.is_active = False
        user.expires_at = timezone.now()
        user.save()
        token = Token.objects.create(user=user)
        send_otp_via_email(user.email, lang=serializer.validated_data.get('message_language', 'EN'))
        return Response({
            'status_code': 200,
            'message': 'Registration successfully check email',
            'token': token.key,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
