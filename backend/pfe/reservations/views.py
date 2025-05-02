# reservations/views.py

from rest_framework import generics, permissions
from django.shortcuts  import get_object_or_404
from .models  import HotelReservation, RestaurantReservation
from .serializers  import HotelReservationSerializer, RestaurantReservationSerializer
from .permissions    import IsClient
from establishements.models  import Hotel, Restaurant


class ListHotelReservations(generics.ListAPIView):
    serializer_class   = HotelReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        hotel = get_object_or_404(Hotel, id=self.kwargs['establishment_id'])
        return HotelReservation.objects.filter(hotel=hotel)


class ListRestaurantReservations(generics.ListAPIView):
    serializer_class   = RestaurantReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        restaurant = get_object_or_404(Restaurant, id=self.kwargs['establishment_id'])
        return RestaurantReservation.objects.filter(restaurant=restaurant)


class AddHotelReservation(generics.CreateAPIView):
    serializer_class   = HotelReservationSerializer
    permission_classes = [permissions.IsAuthenticated, IsClient]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['establishment'] = get_object_or_404(Hotel, id=self.kwargs['establishment_id'])
        return ctx

    def perform_create(self, serializer):
        hotel = self.get_serializer_context()['establishment']
        # assume your Profile is accessible via request.user.profile
        guest = self.request.user.profile
        serializer.save(hotel=hotel, guest=guest)


class AddRestaurantReservation(generics.CreateAPIView):
    serializer_class   = RestaurantReservationSerializer
    permission_classes = [permissions.IsAuthenticated, IsClient]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['establishment'] = get_object_or_404(Restaurant, id=self.kwargs['establishment_id'])
        return ctx

    def perform_create(self, serializer):
        restaurant = self.get_serializer_context()['establishment']
        guest      = self.request.user.profile
        serializer.save(restaurant=restaurant, guest=guest)
