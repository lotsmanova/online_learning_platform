from django.urls import reverse
from rest_framework.test import APITestCase

from course.models import Course
from users.models import User


class BaseTestCase(APITestCase):
    email = 'test@mail.ru'
    password = '12345'
    def setUp(self) -> None:
        self.user = User.objects.create(
            email=self.email
        )

        self.user.set_password(self.password)
        self.user.save()

        response = self.client.post(
            reverse('users:token_obtain_pair'),
            {
                'email': self.email,
                'password': self.password
            }
        )

        self.token = response.json().get('access')

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.course = Course.objects.create(
            title='Test course',
            description='Test course',
        )