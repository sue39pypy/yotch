from rest_framework import serializers
from .models import Dish, Skill, Slide, Wallpaper

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            'title',
            'image_path',
            'caption_converted',
            'url',
            'rank'
        )

class DishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            'title',
            'image_path',
            'caption_converted',
            'url',
            'rank'
        )

    image_path = serializers.SerializerMethodField()
    caption_converted = serializers.SerializerMethodField()

    def get_image_path(self, obj):
        return '/media/' + str(obj.image)

    def get_caption_converted(self, obj):
        return obj.caption.splitlines()

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            'name',
            'icon',
            'level',
            'caption_converted',
            'rank'
        )

class SkillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            'name',
            'icon',
            'level',
            'caption_converted',
            'rank'
        )

    caption_converted = serializers.SerializerMethodField()

    def get_caption_converted(self, obj):
        return obj.caption.splitlines()

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