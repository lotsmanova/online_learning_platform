from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from course.models import Course, Lesson
from subscribes.models import SubscribeUpdate


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
