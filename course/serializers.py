from rest_framework import serializers

from course.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()


    class Meta:
        model = Course
        fields = '__all__'


    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
