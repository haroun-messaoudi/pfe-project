from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import Profile
from establishements.models import Restaurant , Hotel
from django.core.exceptions import ValidationError


class HotelReservation(models.Model) :

    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',)
    checkeIn_date = models.DateTimeField()
    numberOfPeople = models.IntegerField(validators=[MinValueValidator(1)])##max value needed look for it
    roomType = models.CharField(max_length=100,default='')
    checkeOut_date = models.DateTimeField()
    
    
    hotel = models.ForeignKey(Hotel , on_delete=models.CASCADE)
    guest = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def confirm(self):
        self.status = 'confirmed'
        self.save()

    def cancel(self):
        self.status = 'cancelled'
        self.save()    

    def clean(self):
        super().clean()
        # only validate when both dates are set
        if self.checkeIn_date and self.checkeOut_date and self.checkeIn_date > self.checkeOut_date:
            raise ValidationError({
                'checkeOut_date': 'Check-out date cannot be before Check-in date.'
            })

class RestaurantReservation(models.Model) :

    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',)
    date = models.DateTimeField()
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