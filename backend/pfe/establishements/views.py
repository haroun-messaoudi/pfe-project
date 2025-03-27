from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied,NotFound
from django.contrib.auth.models import User
from .models import Hotel,Restaurant,Establishement,Table,Room,MenuItem
from .permissions import IsAssociatedWithEstablishement,IsAssociatedWithHotel,IsAssociatedWithRestaurant,IsOWner
from . import serializers
from django.shortcuts import get_object_or_404
# Create your views here.

class EstablishementCreationView(generics.CreateAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAuthenticated,IsOWner]

    def perform_create(self, serializer):
        if hasattr(self.request.user.profile, "establishement"):
            raise PermissionDenied("You already have an establishement.")
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
        
class EstablishementDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Establishement.objects.all()

class HotelDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.HotelDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Hotel.objects.all()
class RestaurantDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.RestaurantDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Restaurant.objects.all()


class EstablishementListView(generics.ListAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Establishement.objects.all()
class HotelListView(generics.ListAPIView):
    serializer_class = serializers.HotelDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Hotel.objects.all()

class RestaurantListView(generics.ListAPIView):
    serializer_class = serializers.RestaurantDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Restaurant.objects.all()


class EstablishementUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]

    def get_queryset(self):
        return Establishement.objects.filer(profille=self.request.user.profile)
class HotelUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.HotelSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithHotel]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Hotel.objects.filter(establishement=establishement)
    
class RestaurantUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]


    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Restaurant.objects.filter(establishement=establishement)

#tables and rooms handling + modifying the hotel and restaurant details view
class MenuItemCreationView(generics.CreateAPIView):
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def perform_create(self, serializer):
        serializer.save(restaurant=self.request.user.profile.establishement.restaurant)

class MenuItemUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return MenuItem.objects.filter(restaurant=establishement.restaurant)

    
class MenuItemDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return MenuItem.objects.filter(restaurant=establishement.restaurant)
    
class TableCreationView(generics.CreateAPIView):
    serializer_class = serializers.TableSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]
    

class RoomCreationView(generics.CreateAPIView):
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithHotel]
    
class TableUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.TableSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Table.objects.filter(restaurant=establishement.restaurant)
    
class RoomUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithHotel]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Room.objects.filter(hotel=establishement.hotel)
    
class TableDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.TableSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Table.objects.filter(restaurant=establishement.restaurant)

class RoomDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithHotel]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Room.objects.filter(hotel=establishement.hotel)
    

# class RestaurantMenuListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request,pk):
#         restaurant = get_object_or_404(Restaurant,pk)
#         menu = MenuItem.objects.filter(restaurant=restaurant)
#         serializer = serializers.MenuItemSerializer(menu,many=True)
#         return Response(serializer.data)
    

# class HotelRoomsListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request,pk):
#         hotel = get_object_or_404(Hotel, pk=pk)
#         room = Room.objects.filter(hotel=hotel)
#         serializer = serializers.RoomSerializer(room,many=True)
#         return Response(serializer.data)
# class RestaurantTablesListView(APIView):
#     permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]
#     def get(self,request,pk):
#         restaurant = get_object_or_404(Restaurant,pk=pk)
#         tables = Table.objects.filter(restaurant=restaurant)
#         serializer = serializers.TableSerializer(tables,many=True)
#         return Response(serializer.data)