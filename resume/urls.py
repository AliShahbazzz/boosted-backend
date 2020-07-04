from django.urls import path
from .import views

app_name = 'resume'

urlpatterns = [
    path('resume/', views.UserResumeListCreateAPIView.as_view(),
         name='resume_list_create_api'),
    path('resume-png/', views.UserResumePNGView.as_view(),
         name='resume_png_api'),
]
