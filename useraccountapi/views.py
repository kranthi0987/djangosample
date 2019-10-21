from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from useraccountapi.TokenSerializer import TokenSerializer, UserSerializer

# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserCreate(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    # permission_classes = (permissions.AllowAny,)
    #
    # queryset = User.objects.all()
    #
    # def post(self, request, *args, **kwargs):
    #     username = request.data.get("username", "")
    #     password = request.data.get("password", "")
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         # login saves the user’s ID in the session,
    #         # using Django’s session framework.
    #         login(request, user)
    #         serializer = TokenSerializer(data={
    #             # using drf jwt utility functions to generate a token
    #             "token": jwt_encode_handler(
    #                 jwt_payload_handler(user)
    #             )})
    #         serializer.is_valid()
    #         return Response(serializer.data)
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    # above one for form data with passing the value
    # user create with by snding the body.json as
    # {
    #     "username": "nate.silver",
    #     "email": "nate.silver@example.com",
    #     "password": "FiveThirtyEight"
    # }
    # above structure
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


# Add these lines to the views.py file
class RegisterUsers(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(data={"message": "username, password and email is required to register a user"},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(data=UserSerializer(new_user).data,
                        status=status.HTTP_201_CREATED)
