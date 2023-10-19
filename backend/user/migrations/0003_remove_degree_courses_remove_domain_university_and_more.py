# Generated by Django 4.2.2 on 2023-06-30 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_course_degree_degree_level_interest_publication_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degree',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='university',
        ),
        migrations.RemoveField(
            model_name='opening',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='opening',
            name='level',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='degree_seeking',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='publications',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='research_area',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='student_interest_level',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Degree',
        ),
        migrations.DeleteModel(
            name='Degree_Level',
        ),
        migrations.DeleteModel(
            name='Domain',
        ),
        migrations.DeleteModel(
            name='Interest',
        ),
        migrations.DeleteModel(
            name='Opening',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
        migrations.DeleteModel(
            name='Univeristy',
        ),
    ]
