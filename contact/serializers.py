from rest_framework import serializers
from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError

# local import here.
from .models import *


# def validate_email(value):
#     """
#     Let's validate the email passed is in the domain "yourdomain.com"
#     """
#     qs = User.objects.filter(email=value)
#     if qs.exists():
#         raise ValidationError("Email Address Already Exists.")


# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True, validators=[validate_email])

#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name',
#                   'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             email=validated_data['email'],
#             username=validated_data['username'],

#             password=(validated_data['password'])
#         )
#         user.set_password(['password'])
#         user.save()
#         return user


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'message']


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'username', 'email', 'password')


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'])
        return user
