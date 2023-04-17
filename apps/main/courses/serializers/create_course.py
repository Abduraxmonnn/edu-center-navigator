# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.courses.models import CourseCategory, Course


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class CourseCreateSerializer(serializers.ModelSerializer):
    category = CourseCategorySerializer(many=False)

    class Meta:
        model = Course
        fields = [
            'category',
            'name',
            'price',
            'course_duration'
        ]
