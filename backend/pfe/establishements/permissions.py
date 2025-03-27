from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsAssociatedWithEstablishement(BasePermission):
    """
    Custom permission to check if the user is associated with an establishement.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if the user has a profile and an associated establishement
        if not hasattr(request.user, "profile") or not hasattr(request.user.profile, "establishement"):
            raise PermissionDenied("You must be associated with an establishement to access this resource.")
        
        return True