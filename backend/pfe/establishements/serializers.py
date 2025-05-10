from rest_framework.serializers import ModelSerializer
from .models import Establishement, Hotel, Restaurant, MenuItem, Cuisine, Table, Room, Amenity,Images
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from reviews.serializers import ReviewSerializer
from phonenumber_field.validators import validate_international_phonenumber
import re
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
        # extra_kwargs = {
        #     "restaurants": {"read_only": True},
        # }

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
    

from rest_framework import serializers
from .models import Table

class TableSerializer(serializers.ModelSerializer):
    # 1) write-only field for incoming uploads
    image = serializers.ImageField(write_only=True, required=True)

    # 2) read-only field for the URL
    image_url = serializers.ImageField(source='image', read_only=True, use_url=True)

    class Meta:
        model = Table
        fields = '__all__'
        extra_kwargs = {
            # keep restaurant read-only
            'restaurant': {'read_only': True},
        }

    def create(self, validated_data):
        # Pop the file off validated_data (ImageField put it there)
        image = validated_data.pop('image', None)
        request = self.context.get('request')
        restaurant = request.user.profile.establishement.restaurant

        # Create the Table instance
        table = Table.objects.create(restaurant=restaurant, **validated_data)

        # Attach the image and save again
        if image:
            table.image = image
            table.save()

        return table



class RoomSerializer(serializers.ModelSerializer):
    # 1) write-only field for incoming uploads, only jpeg/png allowed
    image = serializers.ImageField(
        write_only=True,
        required=True,
    )

    # 2) read-only field for the URL
    image_url = serializers.ImageField(
        source='image',
        read_only=True,
        use_url=True
    )

    class Meta:
        model = Room
        fields = '__all__'
        extra_kwargs = {
            # keep hotel relation read-only
            'hotel': {'read_only': True},
        }

    def create(self, validated_data):
        # extract the uploaded file
        image = validated_data.pop('image')
        request = self.context.get('request')
        hotel = request.user.profile.establishement.hotel

        # create the Room instance
        room = Room.objects.create(hotel=hotel, **validated_data)

        # attach and save the image
        room.image = image
        room.save()

        return room


class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"
        extra_kwargs = {
            "establishement": {"read_only": True},
        }

class ImageServeSerializer(ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Images
        fields = ['id', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)


class EstablishementSerializer(ModelSerializer):
    images = ImagesSerializer(many=True,required=False)
    reviews = ReviewSerializer(many=True,read_only=True)
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
    def validate(self, attrs):
        if self.instance is None:
            # creation
            if not self.initial_data.get('images'):
                raise serializers.ValidationError({"images": "You must provide at least one image."})
        else:
            # update logic
            if not Images.objects.filter(establishement=self.instance).exists():
                raise serializers.ValidationError({"images": "Establishment must have at least one image."})
        return attrs

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

class EstablishementDetailsSerializer(ModelSerializer):
    restaurant = RestaurantDetailSerializer(read_only=True)
    hotel = HotelDetailsSerializer(read_only=True)
    images = serializers.SerializerMethodField() 
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Establishement
        fields = "__all__"
        extra_kwargs = {
            "average_rating": {"read_only": True},
            "profile": {"read_only": True},
        }

    def get_images(self, obj):
        request = self.context.get('request')
        image_qs = Images.objects.filter(establishement=obj)
        return [
            request.build_absolute_uri(image.image.url)
            for image in image_qs
            if image.image
        ]
    def to_representation(self, instance):
        """
        Customize the representation to include either the restaurant or hotel details
        based on the type of the establishment.
        """
        representation = super().to_representation(instance)
        if hasattr(instance, "restaurant"):
            representation["details"] = self.fields["restaurant"].to_representation(instance.restaurant)
        elif hasattr(instance, "hotel"):
            representation["details"] = self.fields["hotel"].to_representation(instance.hotel)
        else:
            representation["details"] = None
        return representation
    




class establishmentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Establishement
        fields = '__all__'
        extra_kwargs = {
            "average_rating": {"read_only": True},
            "profile": {"read_only": True},
        }