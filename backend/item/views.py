from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Interior
from .renderers import InteriorJSONRenderer
from .serializers import InteriorListSerializer, InteriorSerializer
from .models import Slide
from .renderers import SlideJSONRenderer
from .serializers import SlideListSerializer, SlideSerializer
from .models import Wallpaper
from .renderers import WallpaperJSONRenderer
from .serializers import WallpaperListSerializer, WallpaperSerializer

class InteriorListAPIView(ListAPIView):
    model = Interior
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