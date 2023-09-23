from rest_framework import serializers

from course.models import Course, Lesson, Payments
from course.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

        validators = [LinkValidator('link_video')]


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source='lesson_set', many=True)
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'


    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'