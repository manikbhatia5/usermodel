# Generated by Django 4.0.6 on 2022-07-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0002_remove_usermodel_description_remove_usermodel_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
