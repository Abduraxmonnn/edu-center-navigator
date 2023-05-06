# Django
from django.shortcuts import get_object_or_404

# Rest-Framework
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.center.models import Center
from apps.main.address.models import Address
from apps.main.courses.models import Course
from apps.main.teacher.models import Teacher


class CenterAddressSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'Center Address for Update Center'
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
        ref_name = 'Center Teacher for Update Center'
        model = Teacher
        fields = [
            'name',
            'description',
            'experience_year',
            'image',
            'number_students'
        ]


class CenterCourseSerializer(serializers.ModelSerializer):
    class Meta:
        # ref_name = 'Center Address for Update Center'
        model = Course
        fields = [
            'category',
            'name',
            'price',
            'course_duration',
        ]

class CenterUpdateSerializer(serializers.ModelSerializer):
    center_address = CenterAddressSerializer(many=False)
    top_teachers = CenterTeacherSerializer(many=True)
    image = serializers.ImageField(required=False)
    courses = CenterCourseSerializer(many=True)

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

    def update(self, instance, validated_data):
        # instance = super(CenterUpdateSerializer, self).update(instance, validated_data)
        center_address = validated_data.pop('center_address', [])
        instance.center_address.district = center_address.get('district', instance.center_address.district)
        instance.center_address.street = center_address.get('street', instance.center_address.street)
        instance.center_address.apartment_letter = center_address.get('apartment_letter', instance.center_address.apartment_letter)
        instance.center_address.apartment_number = center_address.get('apartment_number', instance.center_address.apartment_number)
        instance.center_address.lat = center_address.get('lat', instance.center_address.lat)
        instance.center_address.lng = center_address.get('lng', instance.center_address.lng)

        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.main_course = validated_data.get('main_course', instance.main_course)
        instance.image = validated_data.get('image', instance.image)
        instance.is_public = validated_data.get('image', instance.is_public)

        top_teachers = validated_data.pop('top_teachers', [])
        for item in range(len(top_teachers)):
            try:
                center_qr = Center.objects.get(name=instance.name)
                center_qr.top_teachers.name = top_teachers[item].get('name')
                center_qr.top_teachers.description = top_teachers[item].get('description')
                center_qr.top_teachers.experience_year = top_teachers[item].get('experience_year')
                center_qr.top_teachers.number_students = top_teachers[item].get('number_students')
            except Exception as ex:
                return Response({
                    'status_code: ': 404,
                    'message: ': 'Teacher Not Found',
                    'error_message: ': ex,
                }, status=status.HTTP_404_NOT_FOUND)

        courses = validated_data.pop('courses')
        for item in range(len(courses)):
            try:
                courses_qr = Center.objects.get(name=instance.name)
                courses_qr.courses.category = courses[item].get('category')
                courses_qr.courses.name = courses[item].get('name')
                courses_qr.courses.price = courses[item].get('price')
                courses_qr.courses.course_duration = courses[item].get('course_duration')
            except Exception as ex:
                return Response({
                    'status_code: ': 404,
                    'message: ': 'Teacher Not Found',
                    'error_message: ': ex,
                }, status=status.HTTP_404_NOT_FOUND)

        instance.save()
        return instance
