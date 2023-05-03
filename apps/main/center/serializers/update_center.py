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


class CenterUpdateSerializer(serializers.ModelSerializer):
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

    def update(self, instance, validated_data):
        # instance = super(CenterUpdateSerializer, self).update(instance, validated_data)
        center_address = instance.center_address
        center_address.district = validated_data.get('district', center_address.district)
        center_address.street = validated_data.get('street', center_address.street)
        center_address.apartment_letter = validated_data.get('apartment_letter', center_address.apartment_letter)
        center_address.apartment_number = validated_data.get('apartment_number', center_address.apartment_number)
        center_address.lat = validated_data.get('lat', center_address.lat)
        center_address.lng = validated_data.get('lng', center_address.lng)

        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.main_course = validated_data.get('main_course', instance.main_course)
        instance.image = validated_data.get('image', instance.image)
        instance.is_public = validated_data.get('image', instance.is_public)

        for item in validated_data.pop('top_teachers'):
            try:
                teacher_qs = Teacher.objects.get(name=instance.top_teachers.name)
            except:
                return Response({
                    'status_code: ': 404,
                    'message: ': 'Teacher Not Found'
                }, status=status.HTTP_404_NOT_FOUND)

            teacher = teacher_qs.first()
            instance.top_teachers.add(teacher)

        for item in validated_data.pop('courses'):
            course_qs = Course.objects.filter(name__iexact=item['name'])

            if course_qs.exists():
                course = course_qs.first()
            else:
                return Response({
                    'status_code: ': 404,
                    'message: ': 'Course Not Found'
                }, status=status.HTTP_404_NOT_FOUND)

            instance.courses.add(course)

        instance.save()
        return instance
