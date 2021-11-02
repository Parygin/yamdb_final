from rest_framework import permissions  # type: ignore


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.method in permissions.SAFE_METHODS
            or request.user.is_staff  # noqa
        ):
            return True


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user or request.user.is_moderator  # noqa
        ):
            return True
