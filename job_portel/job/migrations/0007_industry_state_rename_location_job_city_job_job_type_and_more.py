# Generated by Django 5.1.4 on 2025-01-27 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_applyjob_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='job',
            old_name='location',
            new_name='City',
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(blank=True, choices=[('Remote', 'Remote'), ('Onsite', 'Onsite'), ('Hybrid', 'Hybrid')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined'), ('Pending', 'Pending')], max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='job.industry'),
        ),
        migrations.AddField(
            model_name='job',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='job.state'),
        ),
    ]
