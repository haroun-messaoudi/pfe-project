# reservations/urls.py

from django.urls import path
from .views      import  ListHotelReservations, ListRestaurantReservations, AddHotelRes,AddRestaurantRes


urlpatterns = [
    path(
      'hotels/<int:establishment_id>',
      ListHotelReservations.as_view(),
      name='hotel-res-list'
    ),
    path(
      'hotels/<int:establishment_id>/add', AddHotelRes.as_view(),name='hotel-res-add'),
    path(
      'restaurants/<int:establishment_id>',
      ListRestaurantReservations.as_view(),
      name='rest-res-list'
    ),
    path(
      'restaurants/<int:establishment_id>/add',
      AddRestaurantRes.as_view(),
      name='rest-res-add'
    ),
]
