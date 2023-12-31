from datetime import datetime, timedelta
from django.utils import timezone

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from course.models import Course, Lesson
from course.paginators import ListPaginator
from course.permissions import IsInModerator, IsUserOwner
from course.serializers import CourseSerializer, LessonSerializer, CourseListSerializer, CourseUpdateSerializer, \
    LessonUpdateSerializer
from subscribes.tasks import sending_mail


class CourseViewSet(viewsets.ModelViewSet):
    default_serializer = CourseSerializer
    serializers = {
        'list': CourseListSerializer,
        'update': CourseUpdateSerializer,
        'retrieve': CourseUpdateSerializer
    }
    queryset = Course.objects.all()
    pagination_class = ListPaginator
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [IsAuthenticated, IsInModerator],
                                    'retrieve': [IsAuthenticated, IsInModerator | IsUserOwner],
                                    'update': [IsAuthenticated, IsInModerator | IsUserOwner],
                                    'destroy': [IsAuthenticated]}

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        new_course = Course.objects.get(id=response.data['id'])
        new_course.owner = self.request.user
        new_course.last_update = datetime.now()
        new_course.save()
        return response


    def perform_update(self, serializer):
        instance = self.get_object()
        subscribe_update = instance.subscribe.get(owner=self.request.user)
        if subscribe_update.is_update_course and instance.last_update - timezone.now() > timedelta(hours=4):
            instance.last_update = timezone.now()
            sending_mail.delay(instance.id, 'Course')
        serializer.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = ListPaginator
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | IsInModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsInModerator | IsUserOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonUpdateSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsInModerator | IsUserOwner]

    def perform_update(self, serializer):
        instance = self.get_object()
        subscribe_update = instance.subscribe.get(owner=self.request.user)
        if subscribe_update.is_update_lesson:
            sending_mail.delay(instance.id, 'Lesson')
        serializer.save()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
