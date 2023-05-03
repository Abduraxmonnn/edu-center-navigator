# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.center.models import Center


class CenterDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = '__all__'
