# Generated by Django 3.0.4 on 2020-03-27 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_sharing', '0006_post_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
    ]
