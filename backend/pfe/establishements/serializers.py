from rest_framework.serializers import ModelSerializer
from .models import Establishement, Hotel, Restaurant, MenuItem, Cuisine, Table, Room, Amenity,Images
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

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

        return Hotel.objects.create(establishement=establishement, **validated_data)

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
        try:
            profile = request.user.profile 
            establishement = profile.establishement  
        except ObjectDoesNotExist:
            raise ValidationError("You must have an establishment to create a restaurant.")
        establishement = request.user.profile.establishement 
        if not hasattr(request.user, "profile") or not hasattr(request.user.profile, "establishement"):
            raise ValidationError("You must be associated with an establishment to create a restaurant.")
        
        if hasattr(establishement, "restaurant") or hasattr(establishement, "hotel"):
            raise ValidationError("This establishement already has a hotel or restaurant.")
        
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

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        extra_kwargs = {
            "hotel": {"read_only": True},
        }
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
