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
            'image'
        )