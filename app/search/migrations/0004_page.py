# Generated by Django 2.2.3 on 2019-11-15 19:46

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_programminglanguage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('title', models.CharField(default='', max_length=255)),
                ('key', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
