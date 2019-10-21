from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = ("username", "email")


    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password')
    #     extra_kwargs = {'password': {'write_only': True}}
    #
    # def create(self, validated_data):
    #     user = User(
    #         email=validated_data['email'],
    #         username=validated_data['username']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
    #

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
