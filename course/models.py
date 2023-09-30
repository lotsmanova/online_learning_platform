from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    prewie = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    last_update = models.DateTimeField(verbose_name='последняя дата обновления', **NULLABLE)

    def __str__(self):
        return f'{self.title}'


    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    prewie = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    link_video = models.CharField(max_length=250, verbose_name='ссылка')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
