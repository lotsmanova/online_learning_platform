from rest_framework.permissions import BasePermission


class IsUpdateProfile(BasePermission):
    # def has_permission(self, request, view):
    #     if view.action == 'retrieve':
    #         return request.user.is_authenticated
    #     elif view.action == 'update':
    #         profile_id = view.kwargs['pk']
    #         return request.user.is_authenticated and request.user.id == profile_id
    #     return False

    def has_object_permission(self, request, view, obj):
        return obj == request.user
