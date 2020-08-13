from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Information
from .renderers import InformationJSONRenderer
from .serializers import InformationListSerializer, InformationSerializer

class InformationListAPIView(ListAPIView):
    model = Information
    queryset = Information.objects.all().order_by('rank')
    permission_classes = (AllowAny, )
    renderer_classes = (InformationJSONRenderer, )
    serializer_class = InformationListSerializer

class InformationRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (InformationJSONRenderer, )
    serializer_class = InformationSerializer

    def retrieve(self, request, information_type, *args, **kwargs):
        information = Information.objects.get(type=information_type)
        serializer = self.serializer_class(information)

        return Response(serializer.data, status=status.HTTP_200_OK)