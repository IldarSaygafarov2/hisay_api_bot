# Generated by Django 4.2.4 on 2023-09-08 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_serviceprofile_verification_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="serviceprofile",
            name="phone_number",
            field=models.CharField(default="", max_length=15),
        ),
    ]
