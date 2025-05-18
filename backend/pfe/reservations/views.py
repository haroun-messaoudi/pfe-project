# reservations/views.py

from rest_framework import generics, permissions , status
from django.shortcuts  import get_object_or_404
from .models  import HotelReservation, RestaurantReservation
from .serializers  import HotelReservationSerializer, RestaurantReservationSerializer
from .permissions    import IsClient , IsOwner
from establishements.models  import Hotel, Restaurant
from rest_framework.exceptions import NotFound , PermissionDenied
from rest_framework.response import Response


class ListHotelReservations(generics.ListAPIView):
    serializer_class   = HotelReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        hotel = get_object_or_404(Hotel, id=self.kwargs['establishment_id'])
        return HotelReservation.objects.filter(room__hotel=hotel)


class ListRestaurantReservations(generics.ListAPIView):
    serializer_class   = RestaurantReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        restaurant = get_object_or_404(Restaurant, id=self.kwargs['establishment_id'])
        return RestaurantReservation.objects.filter(table__restaurant=restaurant)


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
        serializer.save(guest=guest)


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
        serializer.save( guest=guest)

class CancelReservation(generics.DestroyAPIView):
    """
    Clients can delete only their own reservations if they are still pending.
    """
    permission_classes = [IsClient]

    def get_object(self):
        reservation_type = self.kwargs['type']
        reservation_id   = self.kwargs['reservation_id']
        guest            = self.request.user.profile

        if reservation_type == 'hotels':
            reservation = get_object_or_404(
                HotelReservation,
                id=reservation_id,
                guest=guest
            )
        elif reservation_type == 'restaurants':
            reservation = get_object_or_404(
                RestaurantReservation,
                id=reservation_id,
                guest=guest
            )
        else:
            raise NotFound(f"Unknown reservation type “{reservation_type}”.")

        if reservation.status != 'pending':
            raise PermissionDenied("Only pending reservations can be cancelled.")
        

        return reservation
    
    
    def destroy(self, request, *args, **kwargs):
        reservation = self.get_object()

        if isinstance(reservation, HotelReservation) and hasattr(reservation, 'room'):
            reservation.room.amount += 1
            reservation.room.save()
        elif isinstance(reservation, RestaurantReservation) and hasattr(reservation, 'table'):
            reservation.table.amount += 1
            reservation.table.save()

        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class DeleteAnyReservation(generics.DestroyAPIView):
    """
    Owners can delete any reservation on their own hotel/restaurant.
    """
    permission_classes = [IsOwner]

    def get_object(self):
        reservation_type = self.kwargs['type']
        reservation_id    = self.kwargs['reservation_id']
        owner  = self.request.user.profile

        if reservation_type == 'hotels':
            return get_object_or_404(
                HotelReservation,
                id=reservation_id,
                room__hotel__owner=owner
            )
        elif reservation_type == 'restaurants':
            return get_object_or_404(
                RestaurantReservation,
                id=reservation_id,
                table__restaurant__owner=owner
            )
        raise NotFound(f"Unknown reservation type “{reservation_type}”.")
    
