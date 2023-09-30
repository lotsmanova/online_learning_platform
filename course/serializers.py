from rest_framework import serializers

from course.models import Course, Lesson
from course.validators import LinkValidator
from subscribes.models import SubscribeUpdate


class LessonSerializer(serializers.ModelSerializer):
    is_update_lesson = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

        validators = [LinkValidator('link_video')]

    def get_is_update_lesson(self, instance):
        try:
            subscribe_update = SubscribeUpdate.objects.get(course=instance)
            return 'подписка на обновления урока активирована' if subscribe_update.is_update_lesson else 'подписка не активирована'
        except SubscribeUpdate.DoesNotExist:
            return 'подписка не активирована'


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'



class CourseListSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    is_update_course = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


    def get_is_update_course(self, instance):
        try:
            subscribe_update = SubscribeUpdate.objects.get(course=instance)

            return True if subscribe_update.is_update_course else False
            # return 'подписка на обновления активирована' if subscribe_update.is_update_course else 'подписка не активирована'
        except SubscribeUpdate.DoesNotExist:
            return 'подписка не активирована'

class CourseUpdateSerializer(serializers.ModelSerializer):
    is_update_course = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_update_course(self, instance):
        try:
            subscribe_update = SubscribeUpdate.objects.get(course=instance)
            return True if subscribe_update.is_update_course else False
            # return 'подписка на обновления активирована' if subscribe_update.is_update_course else 'подписка не активирована'
        except SubscribeUpdate.DoesNotExist:
            return 'подписка не активирована'
