from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
import os
from django.db.models import Avg
from .choices import ALGERIAN_CITIES

# Create your models here.

class Establishement(models.Model):
    ESTABLISHEMENT_TYPES= (
        ('hotel','Hotel'),
        ('restaurant','Restaurant')
        )

    name = models.CharField(max_length=50)
    profile = models.OneToOneField("accounts.profile",on_delete=models.CASCADE,related_name="establishement")
    location = models.TextField()
    phone_number = PhoneNumberField(region="DZ",null=True,blank=True)
    email = models.EmailField(max_length=254)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1
                                         ,validators=[MinValueValidator(1.0),
                                                      MaxValueValidator(5.0)
                                                      ],default=1.0,null=True,blank=True)
    type = models.CharField(max_length=50,choices=ESTABLISHEMENT_TYPES)
    city = models.CharField(max_length=50,choices=ALGERIAN_CITIES,default="Médéa",null=True,blank=True)
    description = models.TextField(null=True,blank=True,default="")
    def get_average_rating(self):
        avg = self.reviews.aggregate(avg=Avg('rating'))['avg']
        self.average_rating = round(avg, 2) if avg is not None else None
        self.save(update_fields=['average_rating']) 
        return self.average_rating
    
    def __str__(self):
        return self.name

"""
this function is used to create a sub directory for each establishement in the media directory 
and add all the images related to the same establishement to it's directory under it's name
"""
def upload_to_establishment_pics(instance, filename):
    establishment_name = instance.establishement.name
    establishment_name = establishment_name.replace(" ", "_").lower()
    upload_path = os.path.join("media", establishment_name, "pics", filename)

    return upload_path

def upload_to_table_pics(instance, filename):
    restaurant_name = instance.restaurant.establishement.name
    restaurant_name = restaurant_name.replace(" ", "_").lower()
    upload_path = os.path.join("media", restaurant_name, "tables", filename)
    
    return upload_path

def upload_to_room_pics(instance, filename):
    hotel_name = instance.hotel.establishement.name
    hotel_name = hotel_name.replace(" ", "_").lower()
    upload_path = os.path.join("media", hotel_name, "tables", filename)

    return upload_path


class Images(models.Model):
    establishement = models.ForeignKey("establishements.Establishement", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to_establishment_pics, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return f"{self.establishement.name}'s image"
    
class Amenity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Hotel(models.Model): 
    establishement = models.OneToOneField(Establishement, on_delete=models.CASCADE, related_name="hotel",)  
    amenities = models.ManyToManyField(Amenity,related_name="hotels")
    checkInTime = models.TimeField(auto_now=False, auto_now_add=False,default="14:00")
    checkOutTime = models.TimeField(auto_now=False, auto_now_add=False,default="12:00")
    stars = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5)
                                            ],default=1)
    def __str__(self):
        return self.establishement.name
 
    


class Restaurant(models.Model):
    establishement = models.OneToOneField(Establishement, on_delete=models.CASCADE, related_name="restaurant",
                                        null=True,blank=True) 
    cuisine = models.ForeignKey('establishements.Cuisine', on_delete=models.CASCADE, related_name="restaurants",blank=True,null=True)

    def __str__(self):
        return self.establishement.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menu_items")
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.name} - {self.price} DA"

class Cuisine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Table(models.Model):
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    amount = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="tables")
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_to_table_pics, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return f"{self.restaurant.establishement.name} table with- {self.capacity} seats"

class Room(models.Model):
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    amount = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=15, decimal_places=0)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    description = models.TextField(null=True, blank=True)
    room_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_to_room_pics, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return f"{self.hotel.establishement.name} Room with- {self.capacity} beds"
