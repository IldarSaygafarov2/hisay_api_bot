# Generated by Django 4.2.4 on 2023-08-29 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_serviceprofile_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprofile',
            name='document_photo',
            field=models.ImageField(blank=True, null=True, upload_to='services/photos/', verbose_name='Фото'),
        ),
    ]
