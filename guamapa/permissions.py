from rest_framework import permissions


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Public: Read only
    Authenticated: Read Only
    Authenticated as staff or admin: Read and Write
    """

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff and request.user.is_active:
            return True

        return False


class IsStaffAndAuthenticatedReadOnly(permissions.BasePermission):
    """
    Publis: No access
    Authenticated: Read Only
    Staff: read and write
    """

    def has_permission(self, request, view):

        if (request.method in permissions.SAFE_METHODS) and request.user.is_active:
            return True

        if request.user.is_staff and request.user.is_active:
            return True

        return False