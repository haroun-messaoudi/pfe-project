from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
import os


# Create your models here.

class Establishement(models.Model):
    ESTABLISHEMENT_TYPES= (
        ('hotel','Hotel'),
        ('restaurant','Restaurant')
        )
    name = models.CharField(max_length=50)
    profile = models.OneToOneField("accounts.profile",on_delete=models.CASCADE)
    location = models.TextField()
    phone_number = PhoneNumberField(region="DZ",null=True,blank=True)
    email = models.EmailField(max_length=254)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1
                                         ,validators=[MinValueValidator(1.0),
                                                      MaxValueValidator(5.0)
                                                      ],default=1.0)
    type = models.CharField(max_length=50,choices=ESTABLISHEMENT_TYPES)

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

class Images(models.Model):
    establishement = models.ForeignKey("establishements.Establishement", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to_establishment_pics, height_field=None, width_field=None, max_length=None)

class Hotel(models.Model):
    pass

class Restaurant(models.Model):
    pass

class Table(models.Model):
    pass

class Room(models.Model):
    pass