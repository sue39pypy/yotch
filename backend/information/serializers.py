from rest_framework import serializers
from .models import Information

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = (
            'name',
            'type',
            'value',
            'url',
            'icon',
            'rank'
        )

class InformationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = (
            'name',
            'type',
            'value',
            'url',
            'icon',
            'rank'
        )
