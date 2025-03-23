from django.urls import path
from .views import UserRegistrationView,ProfileUpdateRetreiveView,UserListView,ProfileListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-registration"),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("list/", UserListView.as_view(), name="user-list"),
    path("profiles/list/", ProfileListView.as_view(), name="profile-list"),
    path("profiles/<int:pk>/",ProfileUpdateRetreiveView.as_view(),name="profile-details"),
]