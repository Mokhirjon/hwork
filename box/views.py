from .serializers import OurSerializer, OurModel
from rest_framework import generics


class OurAPIView(generics.ListAPIView):
    queryset = OurModel.objects.all()
    serializer_class = OurSerializer
