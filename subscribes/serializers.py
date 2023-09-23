from rest_framework import serializers

from subscribes.models import Subscribe_update


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe_update
        fields = '__all__'