# Generated by Django 4.2.4 on 2023-09-19 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_simpleuserprofile_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simpleuserprofile',
            name='service',
        ),
    ]