# Generated by Django 4.0.6 on 2022-07-21 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0010_alter_employee_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='userId',
        ),
    ]
