from rest_framework import serializers

from course.models import Course, Lesson, Payments, Subscribe_update
from course.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

        validators = [LinkValidator('link_video')]


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe_update
        fields = '__all__'


class CourseListSerializers(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    is_update = serializers.SerializerMethodField()
    # is_update = SubscribeSerializer()

    class Meta:
        model = Course
        fields = '__all__'


    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


    def get_is_update(self, instance):
        if instance:
            return 'подписка на обновления активирована'
        return 'подписка не активирована'


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


