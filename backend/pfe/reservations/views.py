# reservations/views.py

from rest_framework import generics, permissions ,status
from rest_framework.views import APIView
from django.shortcuts  import get_object_or_404
from .models  import HotelReservation, RestaurantReservation
from .serializers  import HotelReservationSerializer, RestaurantReservationSerializer
from .permissions    import IsClient , IsOwner
from establishements.models  import Hotel, Restaurant
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from establishements.models import Establishement
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


class ListOwnerReservations(APIView):
    permission_classes = [IsOwner]

    def get(self, request):
        # 1) grab your Establishement object
        establishment = request.user.profile.establishement

        if establishment.type == "restaurant":
            # 2a) directly filter by the chain: reservation → table → restaurant → establishment
            reservations = RestaurantReservation.objects.filter(
                table__restaurant__establishement=establishment
            )
            serializer = RestaurantReservationSerializer(reservations, many=True)

        elif establishment.type == "hotel":
            # 2b) same idea for hotel → room → hotel → establishment
            reservations = HotelReservation.objects.filter(
                room__hotel__establishement=establishment
            )
            serializer = HotelReservationSerializer(reservations, many=True)

        else:
            return Response(
                {"detail": "Unsupported establishment type."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(serializer.data, status=status.HTTP_200_OK)

class ListClientReservations(APIView):
    permission_classes = [permissions.IsAuthenticated, IsClient]

    def get(self,request):
        restaurant_reservations = RestaurantReservation.objects.filter(guest=request.user.profile)
        hotel_reservations = HotelReservation.objects.filter(guest=request.user.profile)
        rest_ser = RestaurantReservationSerializer(restaurant_reservations, many=True)
        hotel_ser = HotelReservationSerializer(hotel_reservations, many=True)

        return Response({
            "restaurant_reservations": rest_ser.data,
            "hotel_reservations":      hotel_ser.data,
        })        

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
    Clients can delete only their own reservations.
    """
    permission_classes = [IsClient]

    def get_object(self):
        reservation_type = self.kwargs['type']
        reservation_id    = self.kwargs['reservation_id']
        guest  = self.request.user.profile

        if reservation_type == 'hotels':
            return get_object_or_404(
                HotelReservation,
                id=reservation_id,
                guest=guest
            )
        elif reservation_type == 'restaurants':
            return get_object_or_404(
                RestaurantReservation,
                id=reservation_id,
                guest=guest
            )
        raise NotFound(f"Unknown reservation type “{reservation_type}”.")

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
                room__hotel__establishement__profile=owner
            )
        elif reservation_type == 'restaurants':
            return get_object_or_404(
                RestaurantReservation,
                id=reservation_id,
                table__restaurant__establishement__profile=owner
            )
        raise NotFound(f"Unknown reservation type “{reservation_type}”.")
    
