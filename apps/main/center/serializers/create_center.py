# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.center.models import Center
from apps.main.address.models import Address
from apps.main.teacher.models import Teacher


class CenterAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'district',
            'street',
            'apartment_letter',
            'apartment_number',
            'lat',
            'lng'
        ]


class CenterTeacherSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Teacher
        fields = [
            'name',
            'description',
            'experience_year',
            'image',
            'number_students'
        ]


class CenterCreateSerializer(serializers.ModelSerializer):
    center_address = CenterAddressSerializer(many=False)
    top_teachers = CenterTeacherSerializer(many=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Center
        fields = [
            'name',
            'slug',
            'center_address',
            'main_course',
            'image',
            'top_teachers',
            'courses',
            'is_public'
        ]
