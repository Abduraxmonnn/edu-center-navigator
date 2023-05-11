# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.center.models import Center
from apps.main.courses.models import Course, CourseCategory
from apps.main.center.serializers.create_center import CenterAddressSerializer, CenterTeacherSerializer


class CenterCourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class CenterCoursesSerializer(serializers.ModelSerializer):
    category = CenterCourseCategorySerializer(many=False)
    
    class Meta:
        model = Course
        fields = [
            'id',
            'categroy',
            'name',
            'price',
            'course_duration',
            'last_updated',
        ]


class CenterListSerializer(serializers.ModelSerializer):
    center_address = CenterAddressSerializer(many=False)
    top_teachers = CenterTeacherSerializer(many=True)
    courses = CenterCoursesSerializer(many=True)

    class Meta:
        model = Center
        fields = [
            'id',
            'name',
            'slug',
            'center_address',
            'main_course',
            'image',
            'top_teachers',
            'courses',
            'is_public',
            'visited',
            'score',
        ]
