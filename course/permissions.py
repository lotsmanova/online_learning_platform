from rest_framework.permissions import BasePermission


class IsInModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists()

class IsUserOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

