import logging
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import sys

from .models import Information
from .renderers import InformationJSONRenderer
from .serializers import InformationListSerializer, InformationSerializer

class InformationListAPIView(ListAPIView):
    model = Information
    queryset = Information.objects.all().order_by('type', 'rank')
    permission_classes = (AllowAny, )
    renderer_classes = (InformationJSONRenderer, )
    serializer_class = InformationListSerializer

class InformationRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (InformationJSONRenderer, )
    serializer_class = InformationSerializer

    def retrieve(self, request, information_id, *args, **kwargs):
        information = Information.objects.get(id=information_id)
        serializer = self.serializer_class(information)

        return Response(serializer.data, status=status.HTTP_200_OK)

class InformationSpecifiedTypeListApiView(ListAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (InformationJSONRenderer, )
    serializer_class = InformationListSerializer

    def get_queryset(self):
        try:
            logger = logging.getLogger('')

            if self.request.GET.get('type'):
                queryset_type = Information.objects.filter(type=self.request.GET.get('type'))
            else:
                queryset_type = Information.objects.all()

            logging.info(queryset_type)

            queryset = queryset_type
            logging.info(queryset)
            return queryset
        except:
            logger.error('情報取得処理に失敗しました。')