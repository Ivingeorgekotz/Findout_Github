# Generated by Django 5.1 on 2024-11-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("findout_app", "0009_delete_imageupload"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicleimage",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="vehicles/"),
        ),
    ]
