from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.EstablishementCreationView.as_view(), name="establishement-create"),
    path("hotel/create/", views.HotelCreationView.as_view(), name="hotel-create"),
    path("restaurant/create/", views.RestaurantCreationView.as_view(), name="restaurant-create"),
    path("details/", views.EstablishementDetailView.as_view(), name="establishement-detail"),
    path("hotel/details/<int:pk>/", views.HotelDetailView.as_view(), name="hotel-detail"),
    path("restaurant/details/<int:pk>/", views.RestaurantDetailView.as_view(), name="restaurant-detail"),
    path("list/", views.EstablishementListView.as_view(), name="establishements-list"),
    path("hotel/list/", views.HotelListView.as_view(), name="hotels-list"),
    path("restaurant/list/", views.RestaurantListView.as_view(), name="restaurants-list"),
    path("update/", views.EstablishementUpdateView.as_view(), name="establishement-update"),
    path("restaurant/update/", views.RestaurantUpdateView.as_view(), name="restaurant-update"),
    path("hotel/update/", views.HotelUpdateView.as_view(), name="hotel-update"),
    path("restaurant/menu/menu-item/update/<int:pk>/", views.MenuItemUpdateView.as_view(), name="menu-item-update"),
    path("restaurant/menu/menu-item/create/", views.MenuItemCreationView.as_view(), name="menu-item-create"),
    path("restaurant/menu/menu-item/delete/<int:pk>/", views.MenuItemDeleteView.as_view(), name="menu-item-create"),
    path("restaurant/table/create/",views.TableCreationView.as_view(),name="table-create"),
    path("restaurant/table/update/<int:pk>/",views.TableUpdateView.as_view(),name="table-update"),
    path("restaurant/table/delete/<int:pk>/",views.TableDeleteView.as_view(),name="table-delete"),
    path("hotel/room/create/",views.RoomCreationView.as_view(),name="room-create"),
    path("hotel/room/update/<int:pk>/",views.RoomUpdateView.as_view(),name="room-update"),
    path("hotel/room/delete/<int:pk>/",views.RoomDeleteView.as_view(),name="room-delete"),
    path("search/", views.EstablishementSearchView.as_view(), name="establishement-search"),
    path("amenities/list/", views.AmenitiesListView.as_view(), name="hotel-search"),
    path("cuisines/list/", views.CuisineListView.as_view(), name="cuisine-list"),
    path("best-restaurants/", views.BestRatedRestaurantsView.as_view(), name="best-restaurants"),
    path("best-hotels/", views.BestRatedHotelsView.as_view(), name="best-hotels"),
    path("tables-and-rooms/",views.EstablishementTablesAndRoomsView.as_view(),name="establishement-tables-rooms"),
    path("<int:establishment_id>/tables/",views.EstablishementTableListView.as_view(),name="establishement-tables"),
    path("<int:establishment_id>/rooms/", views.EstablishementRoomListView.as_view(),name="establishement_rooms"),
    path(
      '<int:pk>/images/',
      views.EstablishmentImagesView.as_view(),
      name='establishment-images'
    ),
]