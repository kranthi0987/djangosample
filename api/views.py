from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView

from .models import Songs, DummyData
from .serializers import SongsSerializer, DummyDataSerilizer
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer


# Create your views here.

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class DummyDataView(generics.ListAPIView):
    """
        Provides a get method handler.
        """
    queryset = DummyData.objects.all()
    serializer_class = DummyDataSerilizer
    permission_classes = (permissions.IsAuthenticated,)
