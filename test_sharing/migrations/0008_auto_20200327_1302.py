# Generated by Django 3.0.4 on 2020-03-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_sharing', '0007_remove_post_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
