# reservations/serializers.py

from rest_framework import serializers
from .models import HotelReservation, RestaurantReservation


class HotelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelReservation
        # explicitly list fields (you can adjust read_only_fields as needed)
        fields = [
            'id',
            'hotel',
            'guest',
            'status',
            'checkeIn_date',
            'checkeOut_date',
            'numberOfPeople',
            'roomType',
            'created_at',
        ]
        read_only_fields = ['id', 'status', 'created_at']

    def validate(self, attrs):
        """
        Ensure that check-in is before check-out.
        """
        check_in = attrs.get('checkeIn_date', getattr(self.instance, 'checkeIn_date', None))
        check_out = attrs.get('checkeOut_date', getattr(self.instance, 'checkeOut_date', None))

        if check_in and check_out and check_in >= check_out:
            raise serializers.ValidationError({
                'checkeOut_date': 'check‐out must be after check‐in.'
            })
        return attrs

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # allow partial updates, but keep status logic in your model methods
        return super().update(instance, validated_data)


class RestaurantReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReservation
        fields = [
            'id',
            'restaurant',
            'guest',
            'status',
            'date',
            'numberOfPeople',
            'tableType',
            'created_at',
        ]
        read_only_fields = ['id', 'status', 'created_at']

    # if you need any cross‐field validation (e.g. party size limits), you
    # can add a validate() here
