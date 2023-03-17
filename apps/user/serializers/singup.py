# Rest-Framework
from rest_framework import serializers

# Project
from apps.user.models import User

class UserSignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'username',
            'dob',
            'phone_number'
            'email',
            'password',
            'is_verified'
        ]

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError
