from django.urls import reverse
from rest_framework import status

from base.tests import BaseTestCase
from course.models import Lesson
from payments.models import Payments


class PaymentsTestCase(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()

        self.payment = Payments.objects.create(
            user=self.user,
            date_payment='2023-08-08',
            paid_course=self.course,
            payment_amount=10000,
            payment_method='Наличные'
        )

    def test_list_payments(self):
        """Тестирование вывода списка платежей"""

        response = self.client.get(
            reverse('payments:payments_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 1, 'date_payment': '2023-08-08', 'payment_amount': 10000, 'payment_method': 'Наличные', 'user': 11, 'paid_lesson': None, 'paid_course': 12}]
        )
