from rest_framework import serializers

from course.models import Lesson, Course
from course.serializers import LessonSerializer, CourseSerializer
from payments.models import Payments
from payments.services import retrieve_session
from users.models import User



class PaymentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class PaymentCreateSerializer(serializers.ModelSerializer):
    lesson = serializers.SlugRelatedField(slug_field='title', queryset=Lesson.objects.all(),
                                          allow_null=True, required=False)
    user = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Payments
        fields = ['payment_amount', 'lesson', 'payment_method', 'user', 'session']


class PaymentRetrieveSerializer(serializers.ModelSerializer):

    link_for_pay = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payments
        fields = ['user', 'date_payment', 'lesson', 'payment_method', 'is_paid', 'session', 'link_for_pay']

    def get_link_for_pay(self, instance):

        if instance.is_paid:
            return None

        session = retrieve_session(instance.session)

        if session.payment_status == 'unpaid' and session.status == 'open':
            return session.url
        else:
            return 'Срок действия платежной сессии истек. Необходимо создать новый платеж'
