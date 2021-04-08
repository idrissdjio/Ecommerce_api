from rest_framework import permissions

class UserProfilePermission(permissions.BasePermission):
    """tell if the user can access a certain data and perform a certain operations"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            """we check if the request is GET then the user has access"""
            return True
        return obj.id == request.user.id

class UserMomentPermission(permissions.BasePermission):
    """Gives access to a certain data to the user"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
