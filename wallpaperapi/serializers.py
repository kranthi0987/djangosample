from rest_framework import serializers

from wallpaperapi.models import TableWallpaperUpload, TableCategory, TableRating


class WallpaperSerlizer(serializers.ModelSerializer):
    class Meta:
        model = TableWallpaperUpload
        fields = '__all__'


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = TableCategory


class RatingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = TableRating
