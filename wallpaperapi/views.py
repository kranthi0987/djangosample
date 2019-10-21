from django.http import Http404
from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from wallpaperapi.models import TableCategory, TableRating, TableWallpaperUpload
from wallpaperapi.serializers import CategorySerilizer, RatingSerilizer, WallpaperSerlizer


class ListCategories(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = TableCategory.objects.all()
    serializer_class = CategorySerilizer


class ListRatings(generics.ListAPIView):
    """
    provide get method hanlder
    """
    queryset = TableRating.objects.all()
    serializer_class = RatingSerilizer


class ListWallpapers(APIView):
    def get(self, request, format=None):
        users = TableWallpaperUpload.objects.all()
        serializer = WallpaperSerlizer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WallpaperSerlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WallpaperDetails(APIView):
    """
         Retrieve, update or delete a user instance.
         """

    def get_object(self, pk):
        try:
            return TableWallpaperUpload.objects.get(pk=pk)
        except TableWallpaperUpload.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = WallpaperSerlizer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = WallpaperSerlizer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        message = '{"message":"Deleted the object"}'
        return Response(message, status=status.HTTP_204_NO_CONTENT)
