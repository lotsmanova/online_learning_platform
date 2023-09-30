from rest_framework import serializers

from subscribes.models import SubscribeUpdate


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeUpdate
        fields = '__all__'
