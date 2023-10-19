# Generated by Django 4.2.2 on 2023-08-19 19:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0018_job_delete_opening'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='interested',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
