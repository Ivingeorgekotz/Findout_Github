# Generated by Django 5.1 on 2024-09-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("findout_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dealer",
            name="user",
        ),
        migrations.AddField(
            model_name="user",
            name="dealer_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="gst_no",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="pan_card_no",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.DeleteModel(
            name="Dealer",
        ),
    ]
