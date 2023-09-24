from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from course.models import Course, Lesson
from course.paginators import ListPaginator
from course.permissions import IsInModerator, IsUserOwner
from course.serializers import CourseSerializer, LessonSerializer, CourseListSerializer


class CourseViewSet(viewsets.ModelViewSet):
    default_serializer = CourseSerializer
    serializers = {
        'list': CourseListSerializer
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
        new_course.save()
        return response



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
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsInModerator | IsUserOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]





