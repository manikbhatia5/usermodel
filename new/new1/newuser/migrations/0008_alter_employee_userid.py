# Generated by Django 4.0.6 on 2022-07-21 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0007_remove_employee_isadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='userId',
            field=models.ForeignKey(blank=b'I00\n', null=True, on_delete=django.db.models.deletion.SET_NULL, to='newuser.usermodel'),
        ),
    ]
