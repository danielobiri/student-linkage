# Generated by Django 4.2.2 on 2023-07-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
