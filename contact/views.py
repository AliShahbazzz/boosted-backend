from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework import status
from django.contrib.auth import authenticate

# Local Import her
from .serializers import (
    # UserSerializer,
    ContactUsSerializer,
    UserDataSerializer,
    UserCreateSerializer,
    UserLoginSerializer
)

from .models import ContactUs

'''
ContactUs api view.
'''


class ContactUsAPIView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


'''
    Register View
'''


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSerializer

    def post(self, request):
        user = UserCreateSerializer(data=request.data)

        if user.is_valid():
            userInstance = user.save()
            token = Token.objects.create(user=userInstance)
            userInstance = UserDataSerializer(userInstance).data

            return Response({
                'user': userInstance,
                'token': token.key
            }, status=status.HTTP_201_CREATED)

        return Response({
            'detail': user.errors['username'][0]
        }, status=status.HTTP_400_BAD_REQUEST)


'''
Login Api
'''


class LoginView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user_qs = User.objects.filter(username=username)
        if user_qs.count() == 0:
            return Response({
                'detail': 'User not found.'
            }, status=status.HTTP_404_NOT_FOUND)
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({
                'detail': 'Incorrect Password'
            }, status=status.HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user=user)
        user = UserDataSerializer(user).data
        return Response({
            'user': user,
            'token': token.key
        }, status=status.HTTP_200_OK)
