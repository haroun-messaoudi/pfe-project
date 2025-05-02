# reservations/urls.py

from django.urls import path
from .views      import  ListHotelReservations, ListRestaurantReservations, AddHotelReservation,AddRestaurantReservation


urlpatterns = [
    path(
      'hotels/<int:establishment_id>',
      ListHotelReservations.as_view(),
      name='hotel-res-list'
    ),
    path(
      'hotels/<int:establishment_id>/add', AddHotelReservation.as_view(),name='hotel-res-add'),
    path(
      'restaurants/<int:establishment_id>',
      ListRestaurantReservations.as_view(),
      name='rest-res-list'
    ),
    path(
      'restaurants/<int:establishment_id>/add',
      AddRestaurantReservation.as_view(),
      name='rest-res-add'
    ),
]
