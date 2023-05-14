# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.center.models import Center
from apps.main.courses.models import Course
from apps.main.center.serializers.create_center import CenterAddressSerializer, CenterTeacherSerializer


class CenterCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CenterRetrieveSerializer(serializers.ModelSerializer):
    center_address = CenterAddressSerializer(many=False)
    top_teachers = CenterTeacherSerializer(many=True)
    courses = CenterCoursesSerializer(many=True)

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
            'is_public',
            'number_students',
            'visited',
            'score',
        ]
