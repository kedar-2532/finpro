from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsStaff
# Create your views here.

class AdminOnlyView(APIView):
    permission_classes = [IsAdmin]

    def get(self,request):
        return Response({'message':'Welcome Admin'})

class StaffOnlyView(APIView):
    permission_classes = [IsStaff]

    def get(self,request):
        return Response({'message':'Welcome Staff or Admin', 'user':request.user.username, 'role':request.user.role})

class AuthenticatedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({'message':'Welcome Logged In User'})
