from rest_framework.serializers import ModelSerializer
from .models import Establishement, Hotel, Restaurant, MenuItem, Cuisine, Table, Room, Amenity,Images
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"
class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
        extra_kwargs = {
            "establishement": {"read_only": True},
        }
    def create(self, validated_data):
        request = self.context.get("request") 
        establishement = request.user.profile.establishement 
        if hasattr(establishement, "restaurant") or hasattr(establishement, "hotel"):
            raise ValidationError("This establishement already has a hotel or restaurant.")
        if establishement.type != "hotel":
            raise ValidationError("This establishement is not a hotel.")
        amenities_data = validated_data.pop("amenities", [])
        hotel = Hotel.objects.create(establishement=establishement, **validated_data)
        hotel.amenities.set(amenities_data)
        return hotel
    


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
        extra_kwargs = {
            "restaurant": {"read_only": True},
        }

class CuisineSerializer(ModelSerializer):
    class Meta:
        model = Cuisine
        fields = "__all__"
        extra_kwargs = {
            "restaurants": {"read_only": True},
        }

class RestaurantSerializer(ModelSerializer):
    menu = MenuItemSerializer(many=True,required=False)
    class Meta:
        model = Restaurant
        fields = "__all__"
        extra_kwargs = {
            "cuisine": {"required": False},
            "establishement": {"read_only": True},
            "id": {"read_only": True},

        }
    
    def create(self, validated_data):
        request = self.context.get("request") 
        profile = request.user.profile 
        establishement = profile.establishement  
        establishement = request.user.profile.establishement 
     
        if hasattr(establishement, "restaurant") or hasattr(establishement, "hotel"):
            raise ValidationError("This establishement already has a hotel or restaurant.")
        if establishement.type != "restaurant":
            raise ValidationError("This establishement is not a restaurant.")
        menu_data = validated_data.pop("menu", [])

        restaurant = Restaurant.objects.create(establishement=establishement, **validated_data)
        for item in menu_data:
            MenuItem.objects.create(restaurant=restaurant, **item)

        return restaurant
    

class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"
        extra_kwargs = {
            "restaurant": {"read_only": True},
        }
    def create(self, validated_data):
        request = self.context.get("request") 
        restaurant = request.user.profile.establishement.restaurant
        return Table.objects.create(restaurant=restaurant, **validated_data)


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        extra_kwargs = {
            "hotel": {"read_only": True},
        }
    
    def create(self, validated_data):
        request = self.context.get("request") 
        hotel = request.user.profile.establishement.hotel
        return Room.objects.create(hotel=hotel, **validated_data)

class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"
        extra_kwargs = {
            "establishement": {"read_only": True},
        }
class EstablishementSerializer(ModelSerializer):
    images = ImagesSerializer(many=True,required=False)
    class Meta:
        model = Establishement
        fields = "__all__"
        extra_kwargs = {
            "average_rating": {"read_only": True},
            "profile": {"read_only": True},
        }
    def create(self, validated_data):
        images_data = self.context.pop("request").FILES
        establishement = Establishement.objects.create(**validated_data)
        for image_data in images_data.getlist("images"):
            Images.objects.create(establishement=establishement, image=image_data)
        return establishement


class RestaurantDetailSerializer(ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True) 
    tables = TableSerializer(many=True, read_only=True)  
    cuisine = CuisineSerializer(read_only=True) 

    class Meta:
        model = Restaurant
        fields = "__all__"

class HotelDetailsSerializer(ModelSerializer):
    amenities = AmenitySerializer(many=True, read_only=True) 
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = "__all__"
        extra_kwargs = {
            "establishement": {"read_only": True},
        }