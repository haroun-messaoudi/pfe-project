from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsClient(BasePermission):
    """
    Custom permission to check if the user is a client.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if not hasattr(request.user, "profile") or not request.user.profile.role == "client":
            raise PermissionDenied("You must be a client to access this resource.")
        return True