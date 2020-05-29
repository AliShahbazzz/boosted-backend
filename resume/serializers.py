from rest_framework import serializers


# local import here.
from .models import *


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResume
        #fields = ['id', 'user', 'name', 'age', 'position', 'profile']
        fields = '__all__'


class ResumeRetrieveUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResume
        #fields = ['id', 'age', 'position', 'profile']
        fields = '__all__'
