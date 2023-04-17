# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.teacher.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'id',
            'name',
            'description',
            'experience_year',
            'image',
            'number_students',
            'center_id'
        ]
