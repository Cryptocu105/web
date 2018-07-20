# Generated by Django 2.0.7 on 2018-07-03 20:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0087_auto_20180621_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='discord_repos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], size=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='discord_webhook_url',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]
