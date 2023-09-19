from rest_framework.permissions import BasePermission


class IsInModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists()
