# Generated by Django 4.2.5 on 2023-09-23 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_subscribe_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe_update',
            name='course',
        ),
        migrations.RemoveField(
            model_name='subscribe_update',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
        migrations.DeleteModel(
            name='Subscribe_update',
        ),
    ]
