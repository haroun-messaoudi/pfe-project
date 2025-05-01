from django.contrib import admin
from .models import HotelReservation
from .models import RestaurantReservation

admin.site.register(HotelReservation)
admin.site.register(RestaurantReservation)