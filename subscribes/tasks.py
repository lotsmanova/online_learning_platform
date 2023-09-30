from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from course.models import Course, Lesson
from users.models import User


@shared_task
def sending_mail(pk, model):
    if model == 'Course':
        instance = Course.objects.filter(pk=pk).first()
    else:
        instance = Lesson.objects.filter(pk=pk).first()

    if instance:
        send_mail(
            subject='Уведомление об обновлении',
            message=f'Был обновлен {instance.title}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.owner.email]
        )


def check_active(*args, **kwargs):
    users = User.objects.filter(is_active=True)
    for user in users:
        if user.last_login - timezone.now() > timedelta(days=30):
            user.is_active = False
            user.save()
