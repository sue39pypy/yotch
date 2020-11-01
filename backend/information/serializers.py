from rest_framework import serializers
from .models import Information

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = (
            'name',
            'name_ja',
            'type',
            'value',
            'url',
            'icon',
            'color',
            'rank'
        )

class InformationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = (
            'name',
            'name_ja',
            'type',
            'value',
            'url',
            'icon',
            'color',
            'rank'
        )
