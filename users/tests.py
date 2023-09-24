from rest_framework import status

from base.tests import BaseTestCase
from course.models import Lesson
from subscribes.models import Subscribe_update


class UserTestCase(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()

        self.subscribe = Subscribe_update.objects.create(
            course=self.course,
            owner=self.user,
            is_update=True
        )

        self.lesson = Lesson.objects.create(
            title='Test lesson',
            description='Test lesson',
            link_video='test.youtube.com',
            course=self.course,
            owner=self.user
        )


    def test_create_user(self):
        """Тестирование создания пользователя"""

        data = {
            'email': 'test3@mail.ru',
            'password': 'test1'
        }

        response = self.client.post(
            '/users/user/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 15, 'username': None, 'email': 'test3@mail.ru', 'phone': None, 'city': None, 'payments': []}
        )



    def test_list_user(self):
        """Тестирование вывода списка пользователей"""

        response = self.client.get(
            '/users/user/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 17, 'username': None, 'email': 'test@mail.ru', 'phone': None, 'city': None, 'payments': []}]
        )


    def test_retrieve_user(self):
        """Тестирование вывода одного пользователя"""

        response = self.client.get(
            f'/users/user/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 18, 'username': None, 'email': 'test@mail.ru', 'phone': None, 'city': None}
        )


    def test_update_user(self):
        """Тестирование обновления пользователя"""

        response = self.client.patch(
            f'/users/user/{self.user.id}/',
            {'id': 19, 'email': 'test_update@mail.ru', 'password': '12345'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 19, 'username': None, 'email': 'test_update@mail.ru', 'phone': None, 'city': None, 'payments': []}
        )


    def test_delete_user(self):
        """Тестирование удаления пользователя"""

        response = self.client.delete(
            f'/users/user/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
