from rest_framework import serializers
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

#local import here.

class RepresentationMixin(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        for key in result:
            if result[key] == None:
                result[key] = 'N/A'
        return result

class NullRepresentationMixin(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        for key in result:
            if result[key] == None:
                result[key] = None
        return result

class UserMixin(object):

        valid_user = None

        def dispatch(self, request, *args, **kwargs):
            try:
                user, token = TokenAuthentication().authenticate(request)
                self.valid_user = user
            except:
                return JsonResponse({"status": 
                                        "Authentication credentials were not provided."}, 
                                                                status=status.HTTP_401_UNAUTHORIZED)
            return super().dispatch(request, *args, **kwargs)
               