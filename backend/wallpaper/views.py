from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Wallpaper
from .renderers import WallpaperJSONRenderer
from .serializers import WallpaperListSerializer, WallpaperSerializer

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