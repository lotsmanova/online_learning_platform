from django.conf import settings
from django.db import models

from course.models import Course
from users.models import NULLABLE


class Subscribe_update(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='ссылка на курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    is_update = models.BooleanField(verbose_name='подписка на обновления', **NULLABLE)


    def __str__(self):
        return f'{self.course} - {self.is_update}'


    class Meta:
        verbose_name = 'подписка на обновления'
        verbose_name_plural = 'подписки на обновления'
