from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from subscribes.models import Subscribe_update
from subscribes.serializers import SubscribeSerializer


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]


class SubscribeDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscribe_update.objects.all()
    permission_classes = [IsAuthenticated]
