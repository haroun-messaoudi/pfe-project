from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsAssociatedWithEstablishement(BasePermission):
    """
    Custom permission to check if the user is associated with an establishement.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if not hasattr(request.user, "profile") or not hasattr(request.user.profile, "establishement"):
            raise PermissionDenied("You must be associated with an establishement to access this resource.")
        
        return True
class IsAssociatedWithHotel(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if not hasattr(request.user, "profile") or not hasattr(request.user.profile, "establishement") or not hasattr(request.user.profile.establishement, "hotel"):
            raise PermissionDenied("You must be associated with a hotel to access this resource.")
        
        return True
class IsAssociatedWithRestaurant(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if not hasattr(request.user, "profile") or not hasattr(request.user.profile, "establishement") or not hasattr(request.user.profile.establishement, "restaurant"):
            raise PermissionDenied("You must be associated with a restaurant to access this resource.")
        return True
    
class IsOWner(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if not hasattr(request.user, "profile") or not request.user.profile.role == "owner":
            raise PermissionDenied("You must be an owner to access this resource.")
        return True