from django.conf import settings
from django.db import models

from course.models import Course, Lesson
from users.models import NULLABLE


class SubscribeUpdate(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='ссылка на курс', **NULLABLE, related_name='subscribe')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='ссылка на урок', **NULLABLE, related_name='subscribe')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    is_update_course = models.BooleanField(verbose_name='подписка на обновления курса', **NULLABLE)
    is_update_lesson = models.BooleanField(verbose_name='подписка на обновления урок', **NULLABLE)


    def __str__(self):
        if self.course:
            return f'{self.course} - {self.is_update_course}'
        return f'{self.lesson} - {self.is_update_lesson}'


    class Meta:
        verbose_name = 'подписка на обновления'
        verbose_name_plural = 'подписки на обновления'
