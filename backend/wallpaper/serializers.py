from rest_framework import serializers
from .models import Wallpaper

class WallpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallpaper
        fields = (
            'name',
            'image'
        )

class WallpaperListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallpaper
        fields = (
            'name',
            'image_path'
        )

    image_path = serializers.SerializerMethodField()

    def get_image_path(self, obj):
        return '/media/' + str(obj.image)