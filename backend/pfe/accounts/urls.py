from django.urls import path
from .views import UserRegistrationView,ProfileUpdateRetreiveView,UserListView,ProfileListView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-registration"),
    path("list/", UserListView.as_view(), name="user-list"),
    path("profiles/list/", ProfileListView.as_view(), name="profile-list"),
    path("profiles/<int:pk>/",ProfileUpdateRetreiveView.as_view(),name="profile-details"),
]