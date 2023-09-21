from django.conf import settings
from django.db import models

from users.models import NULLABLE, User


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    prewie = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

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


class Payments(models.Model):

    PAY_CHOICES = (
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date_payment = models.DateField(verbose_name='дата платежа')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, choices=PAY_CHOICES, verbose_name='способ оплаты', default='Наличные')


    def __str__(self):
        return f'{self.user}: {self.paid_course or self.paid_lesson}'


    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

