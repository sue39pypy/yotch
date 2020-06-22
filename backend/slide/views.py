from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Slide
from .renderers import SlideJSONRenderer
from .serializers import SlideListSerializer, SlideSerializer

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