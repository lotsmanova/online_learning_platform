from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@mail.ru',
            password='12345'
        )

        self.course = Course.objects.create(
            title='Test course',
            description='Test course',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title='Test lesson',
            description='Test lesson',
            link_video='test.youtube.com',
            course=self.course,
            owner=self.user
        )

        # авторизация пользователя
        self.client.force_authenticate(user=self.user)


    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {
            'title': 'Test',
            'description': 'Test',
            'link_video': 'test.mylink.com',
            'course': self.course.id,
            'owner': self.user.id
        }

        response = self.client.post(
            reverse('course:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 2, 'title': 'Test', 'prewie': None, 'description': 'Test', 'link_video': 'test.mylink.com',
             'course': 1, 'owner': 1}
        )


    def test_list_lesson(self):
        response = self.client.get(
            reverse('course:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 1, 'title': 'Test lesson', 'prewie': None, 'description': 'Test lesson', 'link_video': 'test.youtube.com',
             'course': 1, 'owner': 1}]
        )


    def test_retrieve_lesson(self):

        response = self.client.get(
            reverse('course:lesson', kwargs={'pk': self.lesson.id})
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'title': 'Test lesson', 'prewie': None, 'description': 'Test lesson', 'link_video': 'test.youtube.com',
             'course': 1, 'owner': 1}
        )


    def test_update_lesson(self):

        response = self.client.patch(
            reverse('course:lesson_update', kwargs={'pk': self.lesson.id}),
            {'title': 'Test update lesson'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


