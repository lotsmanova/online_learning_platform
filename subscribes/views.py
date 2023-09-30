from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from subscribes.models import SubscribeUpdate
from subscribes.serializers import SubscribeSerializer


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]


class SubscribeDestroyAPIView(generics.DestroyAPIView):
    queryset = SubscribeUpdate.objects.all()
    permission_classes = [IsAuthenticated]
