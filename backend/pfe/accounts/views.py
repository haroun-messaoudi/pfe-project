from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserProfileSerializer
# Create your views here.

"""
All the work is done in the serializers.py
"""
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    
#only if you want to change the response
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True) 
    #     self.perform_create(serializer)  
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    