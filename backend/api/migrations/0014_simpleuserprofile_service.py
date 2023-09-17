# Generated by Django 4.2.4 on 2023-09-17 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_serviceprofile_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleuserprofile',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.service'),
        ),
    ]
