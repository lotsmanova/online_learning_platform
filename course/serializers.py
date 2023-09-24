from rest_framework import serializers

from course.models import Course, Lesson
from course.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

        validators = [LinkValidator('link_video')]


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'



class CourseListSerializers(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    is_update = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


    def get_is_update(self, instance):
        if instance:
            return 'подписка на обновления активирована'
        return 'подписка не активирована'

