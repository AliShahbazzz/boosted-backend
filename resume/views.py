from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status

# Local Import her
from .serializers import (
    ResumeSerializer,
    ResumeRetrieveUpdateDeleteSerializer
)

from .models import *
from core.mixins import UserMixin


'''
Resume List create api view.
'''


class UserResumeListCreateAPIView(
    # UserMixin,
        ListCreateAPIView):
    queryset = UserResume.objects.all()
    serializer_class = ResumeSerializer

# def create(self, request, *args, **kwargs):
#   serializer = self.get_serializer(data=request.data)
#  serializer.is_valid(raise_exception=True)
# serializer.save(user=self.valid_user)
# return Response({'save': 'success'},
#                                       status=status.HTTP_201_CREATED)


'''
Resume Retrieve and update delete api. 
'''


class UserResumeRetrieveUpdateDeleteApiView(UserMixin, RetrieveUpdateDestroyAPIView):
    queryset = UserResume.objects.all()
    serializer_class = ResumeRetrieveUpdateDeleteSerializer
