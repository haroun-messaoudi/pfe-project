from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied,NotFound
from django.contrib.auth.models import User
from .models import Hotel,Restaurant,Establishement
from .permissions import IsAssociatedWithEstablishement
from . import serializers
# Create your views here.

class EstablishementCreationView(generics.CreateAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

class HotelCreationView(generics.CreateAPIView):
    serializer_class = serializers.HotelSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]
    
    def get_queryset(self):
        return Restaurant.objects.filter(establishement=self.request.user.profile.establishement)
   
class RestaurantCreationView(generics.CreateAPIView):
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]
    queryset = Restaurant.objects.none()
        
class EstablishementDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.profile.establishement

class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.HotelSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]
    queryset = Restaurant.objects.none()
class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Restaurant.objects.filter(establishement=establishement)

class EstablishementListView(generics.ListAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = serializers.Establishement.objects.all()
class HotelListView(generics.ListAPIView):
    serializer_class = serializers.HotelSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = serializers.Hotel.objects.all()
class RestaurantListView(generics.ListAPIView):
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = serializers.Restaurant.objects.all()

class EstablishementUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Establishement.objects.filer(profille=self.request.user.profile)
class HotelUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.HotelSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Hotel.objects.filter(establishement=establishement)
class RestaurantUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]


    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Restaurant.objects.filter(establishement=establishement)

#tables and rooms handling + modifying the hotel and restaurant details view