from rest_framework import serializers
from .models import Selector

class SelectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selector
        fields = (
            'type',
            'value',
            'label',
            'rank'
        )

class SelectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selector
        fields = (
            'type',
            'value',
            'label',
            'rank'
        )
