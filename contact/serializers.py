from rest_framework import serializers

#local import here.
from .models import *

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'message']
