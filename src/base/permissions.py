from rest_framework import permissions

class IsAuthor(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAdminOrAuthor(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.author == request.user