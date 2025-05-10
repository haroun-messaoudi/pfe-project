from django.urls import path
from .views import UserRegistrationView,login_view,ProfileUpdateRetreiveView,UserListView,ProfileListView,UserDetails
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenBlacklistView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-registration"),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("list/", UserListView.as_view(), name="user-list"),
    path("details/", UserDetails.as_view(), name="user-details"),
    path("profiles/list/", ProfileListView.as_view(), name="profile-list"),
    path("profiles/update-details/",ProfileUpdateRetreiveView.as_view(),name="profile-details"),
    path('blacklist/', TokenBlacklistView.as_view(), name='blacklist'),
    path('login/',login_view , name='login')
]