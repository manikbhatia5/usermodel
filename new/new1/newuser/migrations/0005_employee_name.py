# Generated by Django 4.0.6 on 2022-07-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0004_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
