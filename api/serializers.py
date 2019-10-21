from rest_framework import serializers
from .models import Songs, DummyData


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")


class DummyDataSerilizer(serializers.ModelSerializer):
    class Meta:
        model = DummyData
        fields = ("title", "data", "image")
