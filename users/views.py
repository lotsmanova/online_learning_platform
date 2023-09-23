from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsUpdateProfile
from users.serializers import UserSerializer, UserRetrieveSerializer, UserUpdateSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]
    default_serializer = UserSerializer
    serializers = {
        'retrieve': UserRetrieveSerializer,
        'update': UserUpdateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    # def get_permissions(self):
    #     if self.action in ['update', 'partial_update']:
    #         self.permission_classes = [IsAuthenticated, IsUpdateProfile]
    #     return super().get_permissions()