# Generated by Django 3.2.8 on 2021-10-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceport', '0016_auto_20211030_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='pipelinelist',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
