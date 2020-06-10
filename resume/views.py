from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from django.shortcuts import render

# Local Import her
from .serializers import (
    ResumeSerializer,
    ResumeRetrieveUpdateDeleteSerializer
)

from .models import *
from core.mixins import UserMixin
from mysite.settings import BASE_DIR
from django.template.loader import render_to_string


'''
Resume List create api view.
'''


class UserResumeListCreateAPIView(ListCreateAPIView):
    queryset = UserResume.objects.all()
    serializer_class = ResumeSerializer

    def post(self, request):
        resumeData = ResumeSerializer(data=request.data)
        name = request.data['name']
        resume_number = request.data['resume_number']

        if resumeData.is_valid():
            resumeDataInstance = resumeData.save()

            htmlobj = render_to_string(
                'resume' + resume_number + '.html', {'data': resumeDataInstance})
            htmlObject = HTML(string=htmlobj)
            cssStyle = CSS(BASE_DIR+'/templates/resume' +
                           resume_number + '.css')
            font_config = FontConfiguration()

            pdfCreatePath = BASE_DIR+'/media/resumes/' + name + \
                '_' + resume_number + '_' + 'Resume.pdf'
            pdfURL = 'http://localhost:8000/media/resumes/' + \
                name + '_' + resume_number + '_' + 'Resume.pdf'

            htmlObject.write_pdf(
                pdfCreatePath,
                stylesheets=[cssStyle],
                font_config=font_config)

            pngCreatePath = BASE_DIR+'/media/thumbnails/' + name + \
                '_' + resume_number + '_' + 'Resume.png'
            pngURL = 'http://localhost:8000/media/thumbnails/' + \
                name + '_' + resume_number + '_' + 'Resume.png'

            htmlObject.write_png(
                pngCreatePath,
                resolution=60,
                stylesheets=[cssStyle],
                font_config=font_config)

            return Response({
                'message': 'Success! PDF has been generated.',
                'directory': pdfURL,
            }, status=status.HTTP_200_OK)

        return Response({'details': resumeData.errors})

    # def get(self, request):

    #     user = request.data['user']  # 'loganpaul@youtube.com'
    #     resume_number = request.data['resume_number']
    #     qs = UserResume.objects.filter(
    #         user=user, resume_number=resume_number).order_by('created').last()
    #     data = ResumeSerializer(qs).data
    #     return Response({
    #         'data': data
    #     })


'''
Resume Retrieve PNG api. 
'''


# class UserResumePNGView(ListAPIView):

#     def get(self, request):
#         name = 'Both Testing'
#         pngPath = []
#         for resume_number in range(1, 16):
#             pngPath[resume_number] = 'http://localhost:8000/media/thumnails/' + \
#                 name + '_' + str(resume_number) + '_' + 'Resume.png'
#             return Response({
#                 'pngPath': pngPath
#             })

#         return Response({'success'})
