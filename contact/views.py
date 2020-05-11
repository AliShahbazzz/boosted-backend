from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    CreateAPIView, 
    )
from rest_framework import status

#Local Import her
from .serializers import (
    UserSerializer,
    ContactUsSerializer,
    )

from .models import ContactUs

'''
Signup api.
'''

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key, 'user':str(serializer.instance)}, 
                                                                        headers=headers,
                                                                            status=status.HTTP_201_CREATED)


'''
ContactUs api view.
'''
class ContactUsAPIView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
