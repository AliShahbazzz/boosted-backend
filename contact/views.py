from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView, 
    )
from rest_framework import status

#Local Import her
from .serializers import (
    ContactUsSerializer,
    )

from .models import ContactUs

'''
ContactUs api view.
'''
class ContactUsAPIView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
