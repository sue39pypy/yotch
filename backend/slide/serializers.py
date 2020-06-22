from rest_framework import serializers
from .models import Slide

class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = (
            'title',
            'image_path',
            'rank'
        )

class SlideListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = (
            'title',
            'image_path',
            'rank'
        )

    image_path = serializers.SerializerMethodField()

    def get_image_path(self, obj):
        return '/media/' + str(obj.image)