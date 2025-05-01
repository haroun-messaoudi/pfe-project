from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import Profile
from establishements.models import Restaurant , Hotel


class HotelReservation(models.Model) :

    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',)
    checkeIn_date = models.DateTimeField(auto_now_add=True)
    numberOfPeople = models.IntegerField(validators=[MinValueValidator(1)])##max value needed look for it
    roomType = models.CharField
    checkeOut_date = models.DateTimeField(auto_now_add=True)
    
    
    hotel = models.ForeignKey(Hotel , on_delete=models.CASCADE)
    guest = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def confirm(self):
        self.status = 'confirmed'
        self.save()

    def cancel(self):
        self.status = 'cancelled'
        self.save()    



class RestaurantReservation(models.Model) :

    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',)
    date = models.DateTimeField(auto_now_add=True)
    numberOfPeople = models.IntegerField(validators=[MinValueValidator(1)])##max value needed look for it
    tableType = models.CharField(max_length=50)


    restaurant = models.ForeignKey(Restaurant , on_delete=models.CASCADE)
    guest = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def confirm(self):
        self.status = 'confirmed'
        self.save()

    def cancel(self):
        self.status = 'cancelled'
        self.save()