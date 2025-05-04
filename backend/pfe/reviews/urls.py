from django.urls import path
from .views import AddReviewView,HotelQuestionsView,RestaurantQuestionsView,ReviewListView,EstablishmentReviewsView

urlpatterns = [
    path('add/<int:establishement_id>/', AddReviewView.as_view(), name='add-review'),
    path('questions/hotel/', HotelQuestionsView.as_view(), name='hotel-questions'),
    path('questions/restaurant/', RestaurantQuestionsView.as_view(), name='restaurant-questions'),
    path('establishment/<int:establishement_id>/', EstablishmentReviewsView.as_view(), name='establishment-reviews'),
    path('list/', ReviewListView.as_view(), name='list-review'),
]