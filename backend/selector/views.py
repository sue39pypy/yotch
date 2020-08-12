from dal import autocomplete
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Selector
from .renderers import SelectorJSONRenderer
from .serializers import SelectorListSerializer, SelectorSerializer

class SelectorListAPIView(ListAPIView):
    model = Selector
    queryset = Selector.objects.all().order_by('rank')
    permission_classes = (AllowAny, )
    renderer_classes = (SelectorJSONRenderer, )
    serializer_class = SelectorListSerializer

class SelectorRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (SelectorJSONRenderer, )
    serializer_class = SelectorSerializer

    def retrieve(self, request, selector_id, type, *args, **kwargs):
        selector = Selector.objects.get(id=selector_id, type=type)
        serializer = self.serializer_class(selector)

        return Response(serializer.data, status=status.HTTP_200_OK)

class SelectorAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self, type):
        if not self.request.user.is_authenticated:
            return Selector.objects.none()

        qs = Selector.objects.get(type=type)
        if self.q:
            qs = qs.filter(label__istartswith=self.q)

        return qs