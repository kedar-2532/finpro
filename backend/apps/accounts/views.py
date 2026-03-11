from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer