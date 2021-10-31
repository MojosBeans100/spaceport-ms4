# Generated by Django 3.2.8 on 2021-10-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceport', '0011_auto_20211023_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipelineresults',
            name='footprint',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pipelineresults',
            name='satellite_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]