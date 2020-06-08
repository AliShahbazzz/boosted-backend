from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status
from rest_framework.views import APIView
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

# Local Import her
from .serializers import (
    ResumeSerializer,
    ResumeRetrieveUpdateDeleteSerializer
)

from .models import *
from core.mixins import UserMixin
from mysite.settings import BASE_DIR


'''
Resume List create api view.
'''


class UserResumeListCreateAPIView(ListCreateAPIView):
    queryset = UserResume.objects.all()
    serializer_class = ResumeSerializer


'''
Resume Retrieve and update delete api. 
'''


class UserResumeRetrieveUpdateDeleteApiView(UserMixin, RetrieveUpdateDestroyAPIView):
    queryset = UserResume.objects.all()
    serializer_class = ResumeRetrieveUpdateDeleteSerializer


class PDFGenerator(APIView):

    def post(self, request):

        htmlObject = HTML(BASE_DIR+'/resumes/resume1.html')
        # htmlObject = HTML(string=request.data['html'])
        cssStyle = CSS(BASE_DIR+'/resumes/resume1.css')
        font_config = FontConfiguration()

        # pdfURL = 'http://localhost:8000/media/'+request.data['username'] +'_Resume.pdf';
        # pdfPath = BASE_DIR+'/media/'+request.data['username'] +'_Resume.pdf';
        pdfURL = 'http://localhost:8000/media/shahbaz_Resume.pdf'
        pdfPath = BASE_DIR+'/media/shahbaz_Resume.pdf'

        htmlObject.write_pdf(
            pdfPath,
            stylesheets=[cssStyle],
            font_config=font_config)

        return Response({
            'message': 'Success! PDF has been generated.',
            'directory': pdfURL
        }, status=status.HTTP_200_OK)
