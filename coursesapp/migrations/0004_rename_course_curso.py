# Generated by Django 4.1.3 on 2022-11-13 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("coursesapp", "0003_course_instructor_course_platform"),
    ]

    operations = [
        migrations.RenameModel(old_name="Course", new_name="Curso",),
    ]
