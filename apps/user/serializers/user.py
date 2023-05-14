# Rest-Framework
from rest_framework import serializers

# Project
from apps.user.models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    message_language = serializers.CharField(
        max_length=2
    )

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'username',
            'phone_number',
            'email',
            'password',
            'is_verified',
            'message_language'
        ]

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class UserLogInSerializer(serializers.ModelSerializer):
    email = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
