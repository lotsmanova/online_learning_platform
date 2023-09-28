from django.db import models

from course.models import Lesson, Course
from users.models import NULLABLE, User


class Payments(models.Model):

    PAY_CHOICES = (
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date_payment = models.DateField(verbose_name='дата платежа', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50, choices=PAY_CHOICES, verbose_name='способ оплаты', default='Наличные')
    is_paid = models.BooleanField(default=False, verbose_name='статус оплаты')
    session = models.CharField(max_length=150, verbose_name='сессия для оплаты', **NULLABLE)

    def __str__(self):
        return f'{self.user}: {self.course or self.lesson}'


    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
