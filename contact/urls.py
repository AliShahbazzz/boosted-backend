from django.urls import path
from .import views

app_name = 'contact'

urlpatterns = [
    path('signup/', views.UserCreate.as_view(), name='signup'),
    path('contact/', views.ContactUsAPIView.as_view(), name='contact'),
    
]