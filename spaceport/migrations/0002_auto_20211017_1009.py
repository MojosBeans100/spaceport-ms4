# Generated by Django 3.2.8 on 2021-10-17 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spaceport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pipelinelist',
            name='AOI',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='cloud_cover',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='freq_interval',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='freq_number',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='output_format',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='resolution',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='pipelinelist',
            name='status',
        ),
    ]
