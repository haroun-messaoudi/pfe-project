from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.EstablishementCreationView.as_view(), name="establishement-create"),
    path("hotel/create/", views.HotelCreationView.as_view(), name="hotel-create"),
    path("restaurant/create/", views.RestaurantCreationView.as_view(), name="restaurant-create"),
    path("details/<int:pk>/", views.EstablishementDetailView.as_view(), name="establishement-detail"),
    path("hotel/details/<int:pk>/", views.HotelDetailView.as_view(), name="hotel-detail"),
    path("restaurant/details/<int:pk>/", views.RestaurantDetailView.as_view(), name="restaurant-detail"),
    path("list/", views.EstablishementListView.as_view(), name="establishements-list"),
    path("hotel/list/", views.HotelListView.as_view(), name="hotels-list"),
    path("restaurant/list/", views.RestaurantListView.as_view(), name="restaurants-list"),
    path("restaurant/update/<int:pk>/", views.RestaurantUpdateView.as_view(), name="restaurant-update"),
    path("hotel/update/<int:pk>/", views.HotelUpdateView.as_view(), name="hotel-update"),
]