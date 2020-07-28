from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

# Local Import her
from .serializers import *

from .models import *
from core.mixins import UserMixin
from core.size_reducer import img_size_reducer, imgpath_to_base64
from core.pdf_gen import pdf, png


'''
Resume List create api view.
'''


class UserResumeListCreateAPIView(ListCreateAPIView):
    queryset = UserResume.objects.all()
    serializer_class = ResumeSerializer

    def post(self, request):
        user = request.data['user']
        name = request.data['name']
        resume_number = request.data['resume_number']
        image_data = request.data['user_resume_image']
        image = ''

        if image_data:
            image = img_size_reducer(image_data, name, resume_number)

        resumeData = ResumeSerializer(data=request.data)

        if resumeData.is_valid():
            resumeDataInstance = resumeData.save(resume_image=image)
            resumeProp = ResumePropertySerializer(data=request.data)

            if resumeProp.is_valid():
                resumeProp.save()
                request_type = request.data['type']
                if request_type == 'pdf':

                    pdfURL = pdf(request, name, resume_number)

                    return Response({
                        'message': 'Success! PDF has been generated.',
                        'directory': pdfURL
                    }, status=status.HTTP_200_OK)

            pngURL = png(request, name, resume_number)
            pngInstance = ResumeThumbnails.objects.create(
                user=user, resume_number=resume_number, path=pngURL)

            return Response({
                'message': 'Success! PNG has been generated.',
            }, status=status.HTTP_200_OK)

        return Response({'details': resumeData.errors})

    def get(self, request, *args, **kwargs):

        user = self.request.query_params.get('user')
        resume_number = self.request.query_params.get('resume_number')
        qs = UserResume.objects.filter(
            user=user, resume_number=resume_number).order_by('created').last()
        prop_qs = ResumeProperties.objects.filter(
            user=user, resume_number=resume_number).order_by('created').last()
        data = ResumeSerializer(qs).data
        propData = ResumePropertySerializer(prop_qs).data
        base64img = ''
        if data['resume_image']:
            base64img = imgpath_to_base64(data['resume_image'])
        return Response({
            'data': data,
            'image': base64img,
            'propData': propData
        })


'''
Resume Retrieve PNG api.
'''


class UserResumePNGView(ListAPIView):
    queryset = ResumeThumbnails.objects.all()
    serializer_class = ResumeThumbnailSerializer

    def get(self, request, *args, **kwargs):
        user = self.request.query_params.get('user')
        qs = ResumeThumbnails.objects.filter(
            user=user).order_by('resume_number', '-created').distinct('resume_number')
        data = ResumeThumbnailSerializer(qs, many=True).data
        return Response({
            'data': data
        })
