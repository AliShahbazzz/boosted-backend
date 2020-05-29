from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .import views

app_name = 'contact'

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('contact/', views.ContactUsAPIView.as_view(), name='contact'),
]
