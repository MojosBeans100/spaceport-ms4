# Generated by Django 3.2.8 on 2021-10-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceport', '0010_alter_pipelinechoice_user_sat_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipelineresults',
            name='footprint',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pipelineresults',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
