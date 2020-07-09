from rest_framework import serializers

# local import here.
from .models import *


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResume
        #fields = ['id', 'user', 'name', 'age', 'position', 'profile']
        fields = '__all__'


class ResumeThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeThumbnails
        fields = '__all__'


class ResumePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeProperties
        fields = '__all__'
