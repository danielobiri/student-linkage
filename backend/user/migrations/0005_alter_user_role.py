# Generated by Django 4.2.2 on 2023-07-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_f_name_user_l_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'student'), ('professor', 'professor')], default='student', max_length=10),
        ),
    ]