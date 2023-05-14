# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.branch.models import Branch
from apps.main.courses.models import Course
from apps.main.branch.serializers.create_branch import BranchAddressSerializer
from apps.main.center.serializers.list_center import CenterListSerializer


class CenterCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'CenterCoursesSerializerForRetrieveBranch'
        model = Course
        fields = '__all__'


class BranchRetrieveSerializer(serializers.ModelSerializer):
    center = CenterListSerializer(many=False)
    branch_address = BranchAddressSerializer(many=False)
    courses = CenterCoursesSerializer(many=True)

    class Meta:
        model = Branch
        fields = [
            'name',
            'slug',
            'center',
            'branch_address',
            'image',
            'courses',
            'is_public',
            'visited',
            'score',
        ]
