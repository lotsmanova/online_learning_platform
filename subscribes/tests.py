from django.urls import reverse
from rest_framework import status

from base.tests import BaseTestCase
from subscribes.models import Subscribe_update


class SubscribesTestCase(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()

        self.subscribe = Subscribe_update.objects.create(
            course=self.course,
            owner=self.user,
            is_update=True
        )


    def test_create_subscribe(self):
        """Тестирование создания обновления подписки"""

        data = {
            'course': self.course.id,
            'owner': self.user.id,
            'is_update': True
        }

        response = self.client.post(
            reverse('subscribes:subscribe_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 2, 'course': 13, 'owner': 12, 'is_update': True}
        )


    def test_delete_subscribe(self):
        """Тестирование удаления подписка"""

        response = self.client.delete(
            reverse('subscribes:subscribe_delete', kwargs={'pk': self.subscribe.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
