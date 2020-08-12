from rest_framework import serializers
from .models import Interior
from .models import Slide
from .models import Wallpaper

class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = (
            'title',
            'image_path',
            'description_converted',
            'rank'
        )

class InteriorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = (
            'title',
            'image_path',
            'description_converted',
            'rank'
        )

    image_path = serializers.SerializerMethodField()
    description_converted = serializers.SerializerMethodField()

    def get_image_path(self, obj):
        return '/media/' + str(obj.image)

    def get_description_converted(self, obj):
        return obj.description.splitlines()

class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = (
            'title',
            'image_path',
            'description_converted',
            'rank'
        )

class SlideListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = (
            'title',
            'image_path',
            'description_converted',
            'rank'
        )

    image_path = serializers.SerializerMethodField()
    description_converted = serializers.SerializerMethodField()

    def get_image_path(self, obj):
        return '/media/' + str(obj.image)

    def get_description_converted(self, obj):
        return obj.description.splitlines()

class WallpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallpaper
        fields = (
            'name',
            'image_path'
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