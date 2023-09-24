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
            response.json()['results'],
            [{'id': 4, 'title': 'Test lesson', 'prewie': None, 'description': 'Test lesson', 'link_video': 'test.youtube.com',
             'course': 3, 'owner': 3}]
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
            {'id': 5, 'title': 'Test lesson', 'prewie': None, 'description': 'Test lesson', 'link_video': 'test.youtube.com',
             'course': 4, 'owner': 4}
        )


    def test_update_lesson(self):

        response = self.client.put(
            reverse('course:lesson_update', kwargs={'pk': self.lesson.id}),
            {'id': 6, 'title': 'Test lesson update', 'description': 'Test lesson update', 'link_video': 'test.youtube.com', 'course': 5, 'owner': 5}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 6, 'title': 'Test lesson update', 'prewie': None, 'description': 'Test lesson update',
             'link_video': 'test.youtube.com',
             'course': 5, 'owner': 5}
        )


    def test_delete_lesson(self):

        response = self.client.delete(
            reverse('course:lesson_delete', kwargs={'pk': self.lesson.id}),

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

