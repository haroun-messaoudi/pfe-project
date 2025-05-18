# reservations/serializers.py

from rest_framework import serializers
from .models import HotelReservation, RestaurantReservation


class HotelReservationSerializer(serializers.ModelSerializer):
    establishment = serializers.SerializerMethodField()
    room_type = serializers.SerializerMethodField()
    class Meta:
        model = HotelReservation
        # explicitly list fields (you can adjust read_only_fields as needed)
        fields = [
            'id',
            'room',
            'guest',
            'status',
            'check_in_date',
            'check_out_date',
            'number_of_people',
            'created_at',
            'establishment',
            'room_type'
        ]
        
        read_only_fields = ['id', 'status', 'created_at','establishment','room_type','guest']
    def get_check_in_date(obj):
        return obj.chek_in_date.strftime('%Y-%m-%d')
    def get_check_out_date(obj):
        return obj.chek_out_date.strftime('%Y-%m-%d')
    
    def get_room_type(self,obj):
        return obj.room.room_type

    def get_establishment(self,obj):
        return obj.room.hotel.establishement.name 

    def validate(self, data):
        """
        Ensure no overlapping booking exists for this room.
        """
        room       = data.get('room')
        start      = data.get('check_in_date')
        end        = data.get('check_out_date')
        exclude_id = getattr(self.instance, 'pk', None)

        overlap_qs = HotelReservation.objects.filter(
            room=room,
            status__in=['pending', 'confirmed'],
            check_out_date__gt=start,
            check_in_date__lt=end
        )
        if exclude_id:
            overlap_qs = overlap_qs.exclude(pk=exclude_id)

        if overlap_qs.exists():
            raise serializers.ValidationError(
                "That room is already booked for the selected dates."
            )
        return data
    # def validate(self, attrs):
    #     """
    #     Ensure that check-in is before check-out.
    #     """
    #     check_in = attrs.get('checkeIn_date', getattr(self.instance, 'checkeIn_date', None))
    #     check_out = attrs.get('checkeOut_date', getattr(self.instance, 'checkeOut_date', None))
        
    #     if check_in and check_out and check_in >= check_out:
    #         raise serializers.ValidationError({
    #             'checkeOut_date': 'check‐out must be after check‐in.'
    #         })
        
    #     room = attrs.get('room' , getattr(self.instance , 'room',None))
    #     numberOfPeople = attrs.get('numberOfPeople' , getattr(self.instance , 'numberOfPeople',None))
    #     if numberOfPeople > room.capacity :
    #         raise serializers.ValidationError ({
    #             'numberOfPeople': f"This room can only accommodate up to {room.capacity} guests."
    #         })
        
    #     ReservationType= attrs.get('ReservationType',getattr(self.instance , 'ReservationType',None))

    #     return attrs
    

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # allow partial updates, but keep status logic in your model methods
        return super().update(instance, validated_data)


class RestaurantReservationSerializer(serializers.ModelSerializer):

    establishment = serializers.SerializerMethodField()
    table_location =  serializers.SerializerMethodField()
    class Meta:
        model = RestaurantReservation
        fields = [
            'id',
            'table',
            'guest',
            'status',
            'date',
            'numberOfPeople',
            'created_at',
            'establishment',
            'table_location'
        ]
        read_only_fields = ['id', 'status', 'created_at','establishment','table_location','guest']

    def get_establishment(self,obj):
        return obj.table.restaurant.establishement.name 
    
    def get_table_location(self,obj):
        return obj.table.location
    