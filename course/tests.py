from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from base.tests import BaseTestCase
from course.models import Course, Lesson
from users.models import User


class CourseTestCase(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()

        self.lesson = Lesson.objects.create(
            title='Test lesson',
            description='Test lesson',
            link_video='test.youtube.com',
            course=self.course,
            owner=self.user
        )


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
            {'id': 3, 'title': 'Test', 'prewie': None, 'description': 'Test', 'link_video': 'test.mylink.com',
             'course': 3, 'owner': 2}
        )


    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(
            reverse('course:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            [{'id': 7, 'title': 'Test lesson', 'prewie': None, 'description': 'Test lesson', 'link_video': 'test.youtube.com',
             'course': 7, 'owner': 6}]
        )


    def test_retrieve_lesson(self):
        """Тестирование вывода одного урока"""

        response = self.client.get(
            reverse('course:lesson', kwargs={'pk': self.lesson.id})
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 9, 'title': 'Test lesson', 'prewie': None, 'description': 'Test lesson', 'link_video': 'test.youtube.com',
             'course': 9, 'owner': 8}
        )


    def test_update_lesson(self):
        """Тестирование обновления урока"""

        response = self.client.put(
            reverse('course:lesson_update', kwargs={'pk': self.lesson.id}),
            {'id': 11, 'title': 'Test lesson update', 'description': 'Test lesson update', 'link_video': 'test.youtube.com', 'course': 11, 'owner': 10}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 11, 'title': 'Test lesson update', 'prewie': None, 'description': 'Test lesson update',
             'link_video': 'test.youtube.com',
             'course': 11, 'owner': 10}
        )


    def test_delete_lesson(self):
        """Тестирование удаления урока"""

        response = self.client.delete(
            reverse('course:lesson_delete', kwargs={'pk': self.lesson.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


    def test_create_course(self):
        """Тестирование создания курса"""

        data = {
            'title': 'Test course',
            'description': 'Test course',
        }

        response = self.client.post(
            '/course/course/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 2, 'lesson': [], 'title': 'Test course', 'prewie': None, 'description': 'Test course', 'owner': None}
        )


    def test_list_course(self):
        """Тестирование вывода списка курсов"""

        response = self.client.get(
            '/course/course/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            [{'id': 6,  'lesson_count': 1, 'is_update': 'подписка не активирована', 'title': 'Test course', 'prewie': None, 'description': 'Test course', 'owner': None}]
        )


    def test_retrieve_course(self):
        """Тестирование вывода одного курса"""

        response = self.client.get(
            f'/course/course/{self.lesson.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 8, 'lesson': [{'id': 8, 'title': 'Test lesson', 'prewie': None, 'description': 'Test lesson', 'link_video': 'test.youtube.com', 'course': 8, 'owner': 7}],
             'title': 'Test course', 'prewie': None, 'description': 'Test course', 'owner': None}
        )


    def test_update_course(self):
        """Тестирование обновления курса"""

        response = self.client.put(
            f'/course/course/{self.lesson.id}/',
            {'id': 10, 'lesson': [{'id': 10, 'title': 'Test lesson', 'description': 'Test lesson',
                                  'link_video': 'test.youtube.com', 'course': 10, 'owner': 9}],
             'title': 'Test update course', 'description': 'Test update course'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 10, 'lesson': [{'id': 10, 'title': 'Test lesson', 'prewie': None, 'description': 'Test lesson',
                                  'link_video': 'test.youtube.com', 'course': 10, 'owner': 9}],
             'title': 'Test update course', 'prewie': None, 'description': 'Test update course', 'owner': None}
        )


    def test_delete_course(self):
        """Тестирование удаления курса"""

        response = self.client.delete(
            f'/course/course/{self.lesson.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

