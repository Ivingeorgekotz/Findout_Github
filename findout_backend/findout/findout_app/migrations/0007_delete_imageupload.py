# Generated by Django 5.1 on 2024-11-13 11:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("findout_app", "0006_imageupload_user_groups_user_user_permissions"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ImageUpload",
        ),
    ]
