# Generated by Django 3.0.8 on 2020-07-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200729_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
