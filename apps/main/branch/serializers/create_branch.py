# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.branch.models import Branch
from apps.main.address.models import Address

class BranchAddressSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'BranchAddressForCreateBranch'
        model = Address
        fields = [
            'district',
            'street',
            'apartment_letter',
            'apartment_number',
            'lat',
            'lng'
        ]

class BranchCreateSerializer(serializers.ModelSerializer):
    branch_address = BranchAddressSerializer(many=False)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Branch
        fields = [
            'name',
            'slug',
            'center',
            'branch_address',
            'image',
            'courses',
            'is_public'
        ]
