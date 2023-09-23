from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from course.models import Course, Lesson, Payments, Subscribe_update
from course.paginators import ListPaginator
from course.permissions import IsInModerator, IsUserOwner
from course.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscribeSerializer, \
    CourseListSerializers


class CourseViewSet(viewsets.ModelViewSet):
    default_serializer = CourseSerializer
    serializers = {
        'list': CourseListSerializers
    }
    queryset = Course.objects.all()
    pagination_class = ListPaginator
    # permission_classes_by_action = {'create': [IsAuthenticated],
    #                                 'list': [IsAuthenticated, IsInModerator],
    #                                 'retrieve': [IsAuthenticated, IsInModerator | IsUserOwner],
    #                                 'update': [IsAuthenticated, IsInModerator | IsUserOwner],
    #                                 'destroy': [IsAuthenticated]}

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


    def create(self, request, *args, **kwargs):
        new_course = super().create(request, *args, **kwargs)
        new_course.owner = self.request.user
        new_course.save()
        return new_course


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    # pagination_class = ListPaginator
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsInModerator]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsInModerator | IsUserOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated, IsInModerator | IsUserOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    # permission_classes = [IsAuthenticated]


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_lesson', 'paid_course', 'payment_method',)
    ordering_fields = ('date_payment',)
    # permission_classes = [IsAuthenticated]


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    # permission_classes = [IsAuthenticated]


class SubscribeDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscribe_update.objects.all()
    # permission_classes = [IsAuthenticated]
