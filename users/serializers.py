from rest_framework import serializers

from course.serializers import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = User
        fields = '__all__'
