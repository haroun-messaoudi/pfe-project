from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied,NotFound
from django.contrib.auth.models import User
from .models import Hotel,Restaurant,Establishement,Table,Room,MenuItem,Amenity,Cuisine,Images
from .permissions import IsAssociatedWithEstablishement,IsAssociatedWithHotel,IsAssociatedWithRestaurant,IsOWner
from . import serializers
from algoliasearch_django import raw_search
from django.db.models import Q
from django.shortcuts import get_object_or_404
# Create your views here.

class EstablishementCreationView(generics.CreateAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAuthenticated,IsOWner]

    def perform_create(self, serializer):
        if hasattr(self.request.user.profile, "establishement"):
            raise PermissionDenied("You already have an establishement.")
        serializer.save(profile=self.request.user.profile)

class HotelCreationView(generics.CreateAPIView):
    serializer_class = serializers.HotelSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]
    
    def get_queryset(self):
        return Restaurant.objects.filter(establishement=self.request.user.profile.establishement)
   
class RestaurantCreationView(generics.CreateAPIView):
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]
    queryset = Restaurant.objects.none()
        
class EstablishementDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.EstablishementDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_profile = self.request.user.profile
        if not hasattr(user_profile, "establishement"):
            raise NotFound("No establishment is associated with the current user.")
        return user_profile.establishement
    
class EstablishementTableListView(generics.ListAPIView):
    """
    GET /establishments/<id>/tables/
    Returns all Table objects belonging to this establishment's restaurant.
    """
    serializer_class   = serializers.TableSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        estab_id = self.kwargs.get('establishment_id')
        if estab_id is None:
            raise NotFound("No establishment_id provided in URL.")
        try:
            estab =Establishement.objects.get(id=estab_id)
        except Establishement.DoesNotExist:
            raise NotFound(f"Establishment with id={estab_id} not found.")

        # filter by the related Restaurant
        return Table.objects.filter(restaurant=estab.restaurant)


class EstablishementRoomListView(generics.ListAPIView):
    """
    GET /establishments/<id>/rooms/
    Returns all Room objects belonging to this establishment's hotel.
    """
    serializer_class   = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        estab_id = self.kwargs.get('establishment_id')
        if estab_id is None:
            raise NotFound("No establishment_id provided in URL.")
        try:
            estab = Establishement.objects.get(id=estab_id)
        except Establishement.DoesNotExist:
            raise NotFound(f"Establishment with id={estab_id} not found.")

        # filter by the related Hotel
        return Room.objects.filter(hotel=estab.hotel)

class HotelDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.HotelDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Hotel.objects.all()
class RestaurantDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.RestaurantDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Restaurant.objects.all()


class EstablishementListView(generics.ListAPIView):
    serializer_class = serializers.EstablishementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Establishement.objects.all()
class HotelListView(generics.ListAPIView):
    serializer_class = serializers.HotelDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Hotel.objects.all()

class RestaurantListView(generics.ListAPIView):
    serializer_class = serializers.RestaurantDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Restaurant.objects.all()


class EstablishementUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.establishmentUpdateSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithEstablishement]

    def get_object(self):
        user_profile = self.request.user.profile
        if not hasattr(user_profile, "establishement"):
            raise NotFound("No establishment is associated with the current user.")
        return user_profile.establishement
class HotelUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.HotelSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithHotel]

    def get_object(self):
        user_profile = self.request.user.profile
        if not hasattr(user_profile, "establishement"):
            raise NotFound("No establishment is associated with the current user.")
        return user_profile.establishement.hotel
    
class RestaurantUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]
    def get_object(self):
        user_profile = self.request.user.profile
        if not hasattr(user_profile, "establishement"):
            raise NotFound("No establishment is associated with the current user.")
        return user_profile.establishement.restaurant

   

#tables and rooms handling + modifying the hotel and restaurant details view
class MenuItemCreationView(generics.CreateAPIView):
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def perform_create(self, serializer):
        serializer.save(restaurant=self.request.user.profile.establishement.restaurant)

class MenuItemUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return MenuItem.objects.filter(restaurant=establishement.restaurant)

    
class MenuItemDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return MenuItem.objects.filter(restaurant=establishement.restaurant)
    
class TableCreationView(generics.CreateAPIView):
    serializer_class = serializers.TableSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]
    

class RoomCreationView(generics.CreateAPIView):
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithHotel]
    
class TableUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.TableSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Table.objects.filter(restaurant=establishement.restaurant)
    
class RoomUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated, IsAssociatedWithHotel]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Room.objects.filter(hotel=establishement.hotel)

    def update(self, request, *args, **kwargs):
        print("Request Data:", request.data)  # Log the incoming request data
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            print("Error during update:", str(e))  # Log the error
            raise
   
class TableDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.TableSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Table.objects.filter(restaurant=establishement.restaurant)

class RoomDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated,IsAssociatedWithHotel]

    def get_queryset(self):
        establishement = self.request.user.profile.establishement
        return Room.objects.filter(hotel=establishement.hotel)
    

# class RestaurantMenuListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request,pk):
#         restaurant = get_object_or_404(Restaurant,pk)
#         menu = MenuItem.objects.filter(restaurant=restaurant)
#         serializer = serializers.MenuItemSerializer(menu,many=True)
#         return Response(serializer.data)
    

# class HotelRoomsListView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request,pk):
#         hotel = get_object_or_404(Hotel, pk=pk)
#         room = Room.objects.filter(hotel=hotel)
#         serializer = serializers.RoomSerializer(room,many=True)
#         return Response(serializer.data)
# class RestaurantTablesListView(APIView):
#     permission_classes = [permissions.IsAuthenticated,IsAssociatedWithRestaurant]
#     def get(self,request,pk):
#         restaurant = get_object_or_404(Restaurant,pk=pk)
#         tables = Table.objects.filter(restaurant=restaurant)
#         serializer = serializers.TableSerializer(tables,many=True)
#         return Response(serializer.data)

class EstablishementSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')  # Default to empty string

        # Get filters from the request
        filters = request.query_params.get('filters', None)
        if filters:
            filters = " AND ".join(filters.split(","))
        else:
            filters = ""

        # Build the params dictionary
        params = {
            "filters": filters
        }

        try:
            # Use empty string if no query — Algolia will still search using filters only
            results = raw_search(Establishement, query or "", params)
            hits = results.get("hits", [])

            return Response({
                "hits": hits,
                "nbHits": results.get("nbHits", 0),
                "processingTimeMS": results.get("processingTimeMS", 0)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
# class EstablishementSearchView(APIView):
#     def get(self, request):
#         query = request.query_params.get('q', '')  # Search query
#         filters = request.query_params.get('filters', '')  # Filters in the format "key:value"

#         # Start with all establishments
#         queryset = Establishement.objects.all()

#         # Apply search query (if provided)
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) | Q(location__icontains=query) | Q(description__icontains=query)
#             )

#         # Apply filters (if provided)
#         if filters:
#             filter_conditions = Q()
#             for filter_item in filters.split(','):
#                 key, value = filter_item.split(':', 1)
#                 print(f"Filter Key: {key}, Filter Value: {value}")  # Debugging
#                 if key == 'type':
#                     filter_conditions &= Q(type=value)
#                 elif key == 'city':
#                     filter_conditions &= Q(city__icontains=value)
#                 elif key == 'restaurant_cuisine':
#                     filter_conditions &= Q(restaurant__cuisine__name__icontains=value)
#                 elif key == 'hotel_amenities':
#                     filter_conditions &= Q(hotel__amenities__name__icontains=value)
#             queryset = queryset.filter(filter_conditions).distinct()

#         # Serialize the results
#         serializer = serializers.EstablishementDetailsSerializer(queryset, many=True)
#         return Response({
#             "hits": serializer.data,
#             "nbHits": queryset.count(),
#             "processingTimeMS": 0  # You can calculate actual processing time if needed
#         }, status=status.HTTP_200_OK)

class AmenitiesListView(generics.ListAPIView):
    serializer_class = serializers.AmenitySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Amenity.objects.all()

class CuisineListView(generics.ListAPIView):
    serializer_class = serializers.CuisineSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Cuisine.objects.all()



class BestRatedHotelsView(APIView):
    def get(self, request):
        try:
            # Query Algolia for all hotels
            params = {
                "filters": "type:hotel",  # Filter for hotels
                "hitsPerPage": 1000,  # Retrieve a large number of results (adjust as needed)
                "attributesToRetrieve": [
                    "objectID", "name", "location", "type", "average_rating", "city","email",
                    "phone_number",
                    "description", "hotel_stars", "hotel_amenities", "hotel_check_in_time", "hotel_check_out_time"
                ],
                "facets": "*",  # Retrieve all facets
                "facetFilters": [["type:hotel"]]  # Ensure only hotels are included
            }
            results = raw_search(Establishement, "", params)
            hits = results.get("hits", [])

            # Sort the results by average_rating in descending order
            sorted_hits = sorted(hits, key=lambda x: x.get("average_rating", 0), reverse=True)

            # Limit to the top 5 results
            top_hits = sorted_hits[:5]

            return Response({
                "hits": top_hits,
                "nbHits": len(top_hits),
                "processingTimeMS": results.get("processingTimeMS", 0)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BestRatedRestaurantsView(APIView):
    def get(self, request):
        try:
            # Query Algolia for all restaurants
            params = {
                "filters": "type:restaurant",  # Filter for restaurants
                "hitsPerPage": 1000,  # Retrieve a large number of results (adjust as needed)
                "attributesToRetrieve": [
                    "objectID", "name", "location", "type", "average_rating", "city","email",
                    "phone_number",
                    "description", "restaurant_cuisine", "restaurant_menu_items"
                ],
                "facets": "*",  # Retrieve all facets
                "facetFilters": [["type:restaurant"]]  # Ensure only restaurants are included
            }
            results = raw_search(Establishement, "", params)
            hits = results.get("hits", [])

            # Sort the results by average_rating in descending order
            sorted_hits = sorted(hits, key=lambda x: x.get("average_rating", 0), reverse=True)

            # Limit to the top 5 results
            top_hits = sorted_hits[:5]

            return Response({
                "hits": top_hits,
                "nbHits": len(top_hits),
                "processingTimeMS": results.get("processingTimeMS", 0)
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class EstablishementTablesAndRoomsView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAssociatedWithEstablishement]

    def get(self, request):
        estab = request.user.profile.establishement
        if not estab:
            return Response({"error": "No establishment associated with this user."},
                            status=status.HTTP_404_NOT_FOUND)

        if estab.type == "hotel":
            rooms = Room.objects.filter(hotel=estab.hotel)
            serializer = serializers.RoomSerializer(
                rooms,
                many=True,
                context={'request': request}
            )
            return Response({"rooms": serializer.data}, status=status.HTTP_200_OK)

        elif estab.type == "restaurant":
            tables = Table.objects.filter(restaurant=estab.restaurant)
            serializer = serializers.TableSerializer(
                tables,
                many=True,
                context={'request': request}
            )
            return Response({"tables": serializer.data}, status=status.HTTP_200_OK)



class EstablishmentImagesView(APIView):
    def get(self, request, pk):
        images = Images.objects.filter(establishement_id=pk)
        serializer = serializers.ImageServeSerializer(images, many=True, context={'request': request})
        return Response(serializer.data)
        