import stripe
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from payments.models import Payments
from payments.permissions import IsOwner
from payments.serializers import PaymentsListSerializer, PaymentCreateSerializer, PaymentRetrieveSerializer
from payments.services import get_session, retrieve_session

stripe.api_key = settings.STRIPE_API_KEY

class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsListSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'course', 'payment_method',)
    ordering_fields = ('date_payment',)
    permission_classes = [IsAuthenticated]


class PaymentsCreateAPIView(generics.CreateAPIView):

    serializer_class = PaymentCreateSerializer
    permission_classes = [IsOwner]
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        lesson = serializer.validated_data.get('lesson')

        if not lesson:
            raise serializer.ValidationError({
                'message_error': 'Необходимо заполнить "lesson"'
            })
        new_pay = serializer.save()
        new_pay.user = self.request.user
        new_pay.session = get_session(new_pay).id
        new_pay.save()


class PaymentsRetrieveAPYView(generics.RetrieveAPIView):
    serializer_class = PaymentRetrieveSerializer
    permission_classes = [IsOwner]
    queryset = Payments.objects.all()

    def get_object(self):
        new_object = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        session = retrieve_session(new_object.session)

        if session.payment_status == 'paid' and session.status == 'complete':
            new_object.is_paid = True
            new_object.save()
        self.check_object_permissions(self.request, new_object)
        return new_object

