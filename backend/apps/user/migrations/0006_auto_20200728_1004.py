# Generated by Django 3.0.8 on 2020-07-28 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200728_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_type',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
