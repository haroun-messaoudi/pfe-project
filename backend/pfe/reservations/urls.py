# reservations/urls.py

from django.urls import path
from .views      import  ListHotelReservations,ListOwnerReservations,DeleteAnyReservation,CancelReservation, ListRestaurantReservations, AddHotelReservation,AddRestaurantReservation,ListClientReservations


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

    
    path(
      '<str:type>/<int:reservation_id>/delete',
      DeleteAnyReservation.as_view(),
      name='delete-reservation'
    ),
    path(
      '<str:type>/<int:reservation_id>/cancel',
      CancelReservation.as_view(),
      name='cancel-reservation'
    ),
    path(
        'client/list/',
        ListClientReservations.as_view(),
        name='client-reservations'

    ),
    path(
        'owner/list/',
        ListOwnerReservations.as_view(),
        name='owner-reservations'

    )
]
