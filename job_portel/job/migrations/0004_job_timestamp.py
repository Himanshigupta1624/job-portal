# Generated by Django 5.1.4 on 2025-01-22 19:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
