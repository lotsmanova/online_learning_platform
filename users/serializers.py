from rest_framework import serializers

from payments.serializers import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(source='payments_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'city', 'payments']


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'city']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
