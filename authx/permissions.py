from rest_framework.permissions import BasePermission


"""Permissions created for limiting the capabilities of a specific users."""


class IsCashierUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role >= 0)


class IsBaristaUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role >= 2)


class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role >= 3)


class IsOwnerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 4 or request.user.is_superuser)


class MenuViewPermission(BasePermission):
    """Limitation for each user connected with displaying the content of the Menu object view"""

    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list']:
            return bool(request.user.is_authenticated and request.user.role >= 1)
        elif view.action in ['update', 'partial_update', 'destroy', 'create']:
            return bool(request.user.is_authenticated and request.user.role >= 2)

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return bool(request.user.is_authenticated and request.user.role >= 1)
        elif view.action in ['update', 'partial_update', 'destroy', 'create']:
            return bool(request.user.is_authenticated and request.user.role >= 2)
