# Generated by Django 4.0.6 on 2022-07-21 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0006_employee_isadmin_employee_userid_alter_employee_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='isAdmin',
        ),
    ]
