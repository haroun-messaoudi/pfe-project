from algoliasearch_django import AlgoliaIndex
import algoliasearch_django as algoliasearch
from algoliasearch_django.decorators import register
from .models import Establishement



@register(Establishement)
class EstablishementIndex(AlgoliaIndex):
    settings = {
        # Fields to search (full-text)
        'searchableAttributes': [
            'name',
            'location',
            'restaurant_menu_items'
        ],
        
        # Fields usable for filtering/faceting
        'attributesForFaceting': [
            'filterOnly(type)',
            'filterOnly(location)',
            'restaurant_cuisine',  # Filter by cuisine
            'hotel_amenities',     # Filter by amenities
        ],
    }


    def get_queryset(self):
        # Ensure only valid establishments are indexed
        return Establishement.objects.all()

    def get_raw_record(self, instance):
        data = {
            'objectID': instance.pk,  # Required field
            'name': instance.name,
            'location': str(instance.location),  # Ensure this is serializable
            'type': instance.type,
            'average_rating': float(instance.average_rating) if instance.average_rating else None,
        }

        # Handle phone number if exists
        if hasattr(instance, 'phone_number') and instance.phone_number:
            data['phone_number'] = str(instance.phone_number)

        # Hotel-specific fields
        if hasattr(instance, 'hotel'):
            data.update({
                'hotel_stars': instance.hotel.stars,
                'hotel_amenities': [amenity.name for amenity in instance.hotel.amenities.all()],
                'hotel_check_in_time': instance.hotel.checkInTime.strftime('%H:%M'),
                'hotel_check_out_time': instance.hotel.checkOutTime.strftime('%H:%M'),
            })

        # Restaurant-specific fields
        if hasattr(instance, 'restaurant'):
            data.update({
                'restaurant_cuisine': instance.restaurant.cuisine.name if instance.restaurant.cuisine else None,
                'restaurant_menu_items': [menu_item.name for menu_item in instance.restaurant.menu_items.all()],
            })

        return data