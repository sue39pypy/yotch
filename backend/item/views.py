from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Dish, Interior, Skill, Slide, Wallpaper, Work
from .renderers import DishJSONRenderer, InteriorJSONRenderer, SkillJSONRenderer, SlideJSONRenderer, WallpaperJSONRenderer, WorkJSONRenderer
from .serializers import DishListSerializer, DishSerializer, InteriorListSerializer, InteriorSerializer, SkillListSerializer, SkillSerializer, SlideListSerializer, SlideSerializer, WallpaperListSerializer, WallpaperSerializer, WorkListSerializer, WorkSerializer

class DishListAPIView(ListAPIView):
    model = Dish
    queryset = Dish.objects.all().order_by('rank')
    permission_classes = (AllowAny, )
    renderer_classes = (DishJSONRenderer, )
    serializer_class = DishListSerializer

class DishRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (DishJSONRenderer, )
    serializer_class = DishSerializer

    def retrieve(self, request, dish_id, *args, **kwargs):
        dish = Dish.objects.get(id=dish_id)
        serializer = self.serializer_class(dish)

        return Response(serializer.data, status=status.HTTP_200_OK)

class InteriorListAPIView(ListAPIView):
    model = Dish
    queryset = Interior.objects.all().order_by('rank')
    permission_classes = (AllowAny, )
    renderer_classes = (InteriorJSONRenderer, )
    serializer_class = InteriorListSerializer

class InteriorRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (InteriorJSONRenderer, )
    serializer_class = InteriorSerializer

    def retrieve(self, request, interior_id, *args, **kwargs):
        interior = Interior.objects.get(id=interior_id)
        serializer = self.serializer_class(interior)

        return Response(serializer.data, status=status.HTTP_200_OK)

class SkillListAPIView(ListAPIView):
    model = Skill
    queryset = Skill.objects.all().order_by('rank')
    permission_classes = (AllowAny, )
    renderer_classes = (SkillJSONRenderer, )
    serializer_class = SkillListSerializer

class SkillRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (SkillJSONRenderer, )
    serializer_class = SkillSerializer

    def retrieve(self, request, skill_id, *args, **kwargs):
        skill = Skill.objects.get(id=skill_id)
        serializer = self.serializer_class(skill)

        return Response(serializer.data, status=status.HTTP_200_OK)

class SlideListAPIView(ListAPIView):
    model = Slide
    queryset = Slide.objects.all().order_by('rank')
    permission_classes = (AllowAny, )
    renderer_classes = (SlideJSONRenderer, )
    serializer_class = SlideListSerializer

class SlideRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (SlideJSONRenderer, )
    serializer_class = SlideSerializer

    def retrieve(self, request, slide_id, *args, **kwargs):
        slide = Slide.objects.get(id=slide_id)
        serializer = self.serializer_class(slide)

        return Response(serializer.data, status=status.HTTP_200_OK)

class WallpaperListAPIView(ListAPIView):
    model = Wallpaper
    queryset = Wallpaper.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (WallpaperJSONRenderer, )
    serializer_class = WallpaperListSerializer

class WallpaperRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (WallpaperJSONRenderer, )
    serializer_class = WallpaperSerializer

    def retrieve(self, request, wallpaper_id, *args, **kwargs):
        wallpaper = Wallpaper.objects.get(id=wallpaper_id)
        serializer = self.serializer_class(wallpaper)

        return Response(serializer.data, status=status.HTTP_200_OK)

class WorkListAPIView(ListAPIView):
    model = Work
    queryset = Work.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (WorkJSONRenderer, )
    serializer_class = WorkListSerializer

class WorkRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (WorkJSONRenderer, )
    serializer_class = WorkSerializer

    def retrieve(self, request, work_id, *args, **kwargs):
        work = Work.objects.get(id=work_id)
        serializer = self.serializer_class(work)

        return Response(serializer.data, status=status.HTTP_200_OK)