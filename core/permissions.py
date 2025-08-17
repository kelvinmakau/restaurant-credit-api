# Defining permissions for the WAITER and ADMIN roles

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    # Allow access or operations only for admin users
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'ADMIN')
    
class IsAdminOrWaiter(BasePermission):
    # Allowing access for users with either ADMIN or WAITER roles
    # Checks if the user is authenticated and is either the admin or waiter
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role in {'ADMIN', 'WAITER'}
        )