from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permessions to show todos to everyone and to only allow owner of an object to edit it
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # So we will allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the todo:
        return obj.created_by == request.user