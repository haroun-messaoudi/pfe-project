from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES = (
        ('client','Client'),
        ('owner','Owner')
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=50,choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True, region="DZ")
    # is_verified = models.BooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return f"{self.user.username}'s profile"
